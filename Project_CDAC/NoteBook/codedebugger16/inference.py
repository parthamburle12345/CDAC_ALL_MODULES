"""
CDAC AI Code Reviewer & Bug Detection Engine
Production Inference SDK & Standalone CLI
"""

import os
import sys
import json
import difflib
import argparse
import torch
from typing import Dict, Any, Optional
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

SYSTEM_PROMPT = """You are an elite Staff Security Engineer and Automated Code Review Engine specializing in C++, Java, and Python.
Your mandate is to analyze code indexed with line prefixes ('1: ', '2: '), detect vulnerabilities, and emit a strict JSON diagnostic audit.
Adhere strictly to the PRD JSON schema with keys: summary, severityScore, issues, and refactoredCode."""

class CodeReviewerEngine:
    def __init__(self, base_model_name: str = "Qwen/Qwen2.5-Coder-7B-Instruct", adapter_path: str = "./final_trilingual_adapter_v15"):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        print(f"Loading tokenizer from {adapter_path if os.path.exists(adapter_path) else base_model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            adapter_path if os.path.exists(adapter_path) else base_model_name,
            trust_remote_code=True
        )
        
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        print(f"Loading Base Model: {base_model_name} on {self.device} (dtype={dtype})...")
        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            torch_dtype=dtype,
            device_map="auto" if torch.cuda.is_available() else None,
            trust_remote_code=True
        )
        
        if os.path.exists(adapter_path):
            print(f"✅ Loading fine-tuned LoRA weights from {adapter_path}...")
            self.model = PeftModel.from_pretrained(base_model, adapter_path)
        else:
            print("⚠️ Adapter not found; running in zero-shot base model mode.")
            self.model = base_model
            
        self.model.eval()
        print("🚀 CodeReviewer Engine Ready!")

    def review_code(self, code: str, language: str = "python", file_path: str = "snippet") -> Dict[str, Any]:
        lines = code.splitlines()
        indexed_code = "\n".join(f"{i+1}: {line}" for i, line in enumerate(lines))
        
        prompt = f"Perform an exhaustive security and bug audit on this {language.upper()} code:\nFile: {file_path}\n\n{indexed_code}"
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        chat_text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(chat_text, return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=1024,
                do_sample=False,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
        gen_text = self.tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()
        
        # Extract JSON
        clean_json = gen_text
        if "```json" in clean_json:
            clean_json = clean_json.split("```json")[1].split("```")[0].strip()
        elif "```" in clean_json:
            clean_json = clean_json.split("```")[1].split("```")[0].strip()
            
        try:
            audit = json.loads(clean_json)
        except Exception:
            audit = {
                "summary": "Review completed (raw text response).",
                "severityScore": 5,
                "issues": [],
                "refactoredCode": code
            }
            
        audit["originalCode"] = code
        refactored = audit.get("refactoredCode", code)
        
        # Calculate unified diff for Monaco Editor
        orig_lines = code.splitlines(keepends=True)
        ref_lines = refactored.splitlines(keepends=True)
        diff = "".join(difflib.unified_diff(orig_lines, ref_lines, fromfile="original", tofile="refactored"))
        audit["diff"] = diff
        return audit

def print_audit_report(result: Dict[str, Any]):
    print("\n" + "=" * 80)
    print("               CDAC AI CODE AUDIT REPORT")
    print("=" * 80)
    print(f"Summary         : {result.get('summary')}")
    print(f"Severity Score  : {result.get('severityScore')}/10")
    print(f"Issues Detected : {len(result.get('issues', []))}")
    for idx, issue in enumerate(result.get("issues", [])):
        print(f"\n  [Issue {idx+1}]")
        print(f"    Lines       : {issue.get('lineStart')}-{issue.get('lineEnd')}")
        print(f"    Severity    : {issue.get('severity')}")
        print(f"    Category    : {issue.get('category')}")
        print(f"    Description : {issue.get('description')}")
        print(f"    Fix         : {issue.get('suggestedFix')}")
        
    diff = result.get("diff", "")
    if diff.strip():
        print("\nUnified Diff (Monaco Editor):")
        print("-" * 80)
        for line in diff.splitlines()[:20]:
            print(f"  {line}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AI Code Reviewer on a source file")
    parser.add_argument("--file", type=str, help="Path to code file to review")
    parser.add_argument("--lang", type=str, default="python", choices=["cpp", "java", "python"], help="Programming language")
    args = parser.parse_args()
    
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            sample_code = f.read()
    else:
        sample_code = """def fetch_user_profile(user_id, cache={}):\n    cache[user_id] = cache.get(user_id, 0) + 1\n    return cache"""
        print("Using demo Python snippet (Mutable Default Argument)...")
        
    engine = CodeReviewerEngine()
    audit_res = engine.review_code(sample_code, language=args.lang)
    print_audit_report(audit_res)
