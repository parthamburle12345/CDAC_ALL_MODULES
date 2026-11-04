"""
CDAC PGCP-AI Code Reviewer & Bug Detection Engine
Production FastAPI Backend Server for React Monaco Editor Integration
Run locally:
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload
"""

import os
import json
import difflib
import torch
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

app = FastAPI(
    title="CDAC Enterprise AI Code Reviewer API (V15)",
    version="1.5.0",
    description="Backend API serving Fine-Tuned Qwen2.5-Coder LoRA for C++, Java, and Python"
)

# Enable CORS for React Frontend (Monaco DiffEditor)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_MODEL_NAME = "Qwen/Qwen2.5-Coder-7B-Instruct"
ADAPTER_PATH = "./final_trilingual_adapter_v15"

print("⏳ Initializing AI Code Reviewer Service...")
device = "cuda:0" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

tokenizer = AutoTokenizer.from_pretrained(
    ADAPTER_PATH if os.path.exists(ADAPTER_PATH) else BASE_MODEL_NAME,
    trust_remote_code=True
)

base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_NAME,
    torch_dtype=dtype,
    device_map="auto" if torch.cuda.is_available() else None,
    trust_remote_code=True
)

if os.path.exists(ADAPTER_PATH):
    print(f"✅ Loading fine-tuned LoRA weights from {ADAPTER_PATH}...")
    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
else:
    print("⚠️ LoRA Adapter not found locally; running in base model mode.")
    model = base_model

model.eval()
print(f"🚀 AI Code Reviewer Backend Online on {device}!")

class CodeReviewRequest(BaseModel):
    code: str = Field(..., description="Raw source code snippet")
    language: str = Field(default="python", description="Language: cpp, java, or python")
    filePath: Optional[str] = Field(default="snippet", description="File path for context")

class CodeIssue(BaseModel):
    lineStart: int
    lineEnd: int
    severity: str
    category: str
    description: str
    suggestedFix: str

class CodeReviewResponse(BaseModel):
    summary: str
    severityScore: int
    issues: List[CodeIssue]
    originalCode: str
    refactoredCode: str
    diff: Optional[str] = None

SYSTEM_PROMPT = """You are an elite Staff Security Engineer and Automated Code Review Engine specializing in C++, Java, and Python.
Your mandate is to analyze code indexed with line prefixes ('1: ', '2: '), detect vulnerabilities, and emit a strict JSON diagnostic audit.
Adhere strictly to the PRD JSON schema with keys: summary, severityScore, issues, and refactoredCode."""

@app.get("/health")
def health():
    return {
        "status": "online",
        "model": BASE_MODEL_NAME,
        "adapter_loaded": os.path.exists(ADAPTER_PATH),
        "device": device
    }

@app.post("/review", response_model=CodeReviewResponse)
def review_code(req: CodeReviewRequest):
    if not req.code.strip():
        raise HTTPException(status_code=400, detail="Empty code snippet provided.")
        
    lines = req.code.splitlines()
    indexed_code = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines))
    
    prompt = f"Perform an exhaustive security and bug audit on this {req.language.upper()} code:\nFile: {req.filePath}\n\n{indexed_code}"
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]
    
    chat_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(chat_text, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=1024,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )
    
    gen_text = tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()
    
    clean_json = gen_text
    if "```json" in clean_json:
        clean_json = clean_json.split("```json")[1].split("```")[0].strip()
    elif "```" in clean_json:
        clean_json = clean_json.split("```")[1].split("```")[0].strip()
        
    try:
        data = json.loads(clean_json)
    except Exception:
        data = {
            "summary": "Review completed (raw model output).",
            "severityScore": 5,
            "issues": [],
            "refactoredCode": req.code
        }
        
    data["originalCode"] = req.code
    if "refactoredCode" not in data or not data["refactoredCode"]:
        data["refactoredCode"] = req.code
        
    orig_lines = req.code.splitlines(keepends=True)
    ref_lines = data["refactoredCode"].splitlines(keepends=True)
    diff = "".join(difflib.unified_diff(orig_lines, ref_lines, fromfile="original", tofile="refactored"))
    data["diff"] = diff
    
    return data
