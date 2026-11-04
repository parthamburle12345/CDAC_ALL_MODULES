"""
CDAC PGCP-AI Code Reviewer & Bug Detection Engine
Production FastAPI Backend Server for React Monaco Editor Integration
Run locally:
    uvicorn app_server:app --host 0.0.0.0 --port 8000 --reload
"""

import os, json, re, difflib, torch
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

app = FastAPI(
    title="CDAC Enterprise AI Code Reviewer API",
    version="1.0.0",
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
ADAPTER_PATH = "./final_trilingual_adapter"

print("⏳ Loading Model & LoRA Adapter for Backend Serving...")
device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(
    ADAPTER_PATH if os.path.exists(ADAPTER_PATH) else BASE_MODEL_NAME,
    trust_remote_code=True
)

if device == "cuda:0":
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME,
        torch_dtype=torch.float16,
        device_map={"": 0},
        trust_remote_code=True
    )
    if os.path.exists(ADAPTER_PATH):
        model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
        print(f"✅ LoRA Adapter loaded from {ADAPTER_PATH}")
    else:
        model = base_model
        print(f"⚠️ Adapter path not found. Running base model {BASE_MODEL_NAME}")
else:
    print("ℹ️ Running on CPU mode (float32)...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
        trust_remote_code=True
    )
    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH) if os.path.exists(ADAPTER_PATH) else base_model

model.eval()
print(f"🚀 Model ready on {device}")

# Production Secret Scanner
SECRET_PATTERNS = [
    ("AWS Access Key", re.compile(r'AKIA[0-9A-Z]{16}')),
    ("AWS Secret Key", re.compile(r'aws_secret_access_key\s*=\s*[A-Za-z0-9/+=]{40}', re.IGNORECASE)),
    ("Generic JWT Token", re.compile(r'eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+')),
    ("Private RSA Key", re.compile(r'-----BEGIN (?:RSA )?PRIVATE KEY-----')),
    ("Database URI with Password", re.compile(r'[a-zA-Z0-9]+://[^:\s]+:[^@\s]+@[^\s]+'))
]

class CodeReviewRequest(BaseModel):
    code: str = Field(..., description="Raw source code to review")
    language: str = Field(..., description="Programming language: cpp, java, or python")

SYSTEM_PROMPT = """You are an Enterprise Principal AI Code Reviewer and Security Architect specializing in polyglot codebases (C++, Java, Python).
Your role is to conduct automated static code audits, identify logic bugs, security vulnerabilities (OWASP Top 10), performance bottlenecks, and style antipatterns, and output your complete evaluation strictly in this runtime-safe JSON schema:

{
  "summary": "<String: Executive assessment of code health>",
  "severityScore": <Integer: 1 (Clean) to 10 (Critical Vulnerability)>,
  "issues": [
    {
      "lineStart": <Integer: 1-based start line>,
      "lineEnd": <Integer: 1-based end line>,
      "severity": "<CRITICAL | HIGH | MEDIUM | LOW>",
      "category": "<SECURITY | BUG | PERFORMANCE | STYLE>",
      "description": "<String: Detailed technical diagnosis>",
      "suggestedFix": "<String: Refactored replacement snippet for faulty section>"
    }
  ],
  "refactoredCode": "<String: Complete, fully compilable refactored file content for Monaco DiffEditor>"
}"""

@app.get("/health")
def health_check():
    return {
        "status": "online",
        "model": BASE_MODEL_NAME,
        "adapter_loaded": os.path.exists(ADAPTER_PATH),
        "device": device
    }

@app.post("/api/review")
def review_code_endpoint(req: CodeReviewRequest):
    # 1. Pre-filter Secret Scanner
    detected_secrets = []
    sanitized_code = req.code
    for name, pattern in SECRET_PATTERNS:
        if pattern.search(sanitized_code):
            detected_secrets.append(name)
            sanitized_code = pattern.sub('[REDACTED_SECRET]', sanitized_code)
            
    # Format numbered code for model
    lines = sanitized_code.strip().split('\n')
    numbered_code = '\n'.join([f'{i+1:3d}: {line}' for i, line in enumerate(lines)])
    
    user_prompt = f"Language: {req.language}\nReview the following source code:\n\n```{req.language}\n{numbered_code}\n```\n\nProvide your complete analysis strictly in the requested JSON format."
    
    chat = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
    prompt_str = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    
    inputs = tokenizer(prompt_str, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=500,
            temperature=0.01,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id
        )
    gen = tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True).strip()
    
    # Parse JSON
    try:
        match = re.search(r'\{.*\}', gen, re.DOTALL)
        if match:
            gen = match.group(0)
        data = json.loads(gen)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse LLM JSON output: {str(e)}")
        
    data["detectedSecrets"] = detected_secrets
    
    # Calculate Unified Diff for Frontend Monaco DiffEditor
    if "refactoredCode" in data:
        diff = list(difflib.unified_diff(
            req.code.splitlines(keepends=True),
            data["refactoredCode"].splitlines(keepends=True),
            fromfile="original",
            tofile="refactored",
            n=1
        ))
        data["diff"] = "".join(diff)
        
    return data