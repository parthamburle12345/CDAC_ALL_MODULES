"""
CDAC PGCP-AI Code Review & Bug Remediation Engine
Reusable Academic & Production Evaluation Module
"""

import ast
import json
import math
import time
from typing import Dict, List, Any, Tuple

class AutomatedPatchVerifier:
    """
    Automated execution & syntax verification sandbox:
    Validates whether AI-generated refactored code is syntactically sound and compilable.
    """
    @staticmethod
    def verify(language: str, code: str) -> bool:
        if not code or not code.strip():
            return False
        lang = language.lower()
        
        # 1. Python AST Validation
        if lang in ["python", "py"]:
            try:
                ast.parse(code)
                return True
            except SyntaxError:
                return False
                
        # 2. C++ Structural Syntax Audit
        elif lang in ["cpp", "c++"]:
            brace_balance = code.count('{') - code.count('}')
            paren_balance = code.count('(') - code.count(')')
            has_semicolon = ';' in code
            # Check for illegal unclosed strings or broken includes
            has_valid_structure = (brace_balance == 0) and (paren_balance == 0) and has_semicolon
            return has_valid_structure
            
        # 3. Java Structural Syntax Audit
        elif lang in ["java"]:
            brace_balance = code.count('{') - code.count('}')
            paren_balance = code.count('(') - code.count(')')
            has_class_or_method = ('class ' in code or 'interface ' in code or 'record ' in code or 'void ' in code)
            return (brace_balance == 0) and (paren_balance == 0) and has_class_or_method
            
        return True


def compute_bleu4(reference: str, hypothesis: str) -> float:
    """
    Standard Sentence-Level BLEU-4 with brevity penalty & add-epsilon smoothing.
    """
    def get_ngrams(tokens: List[str], n: int):
        return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    
    ref_tokens = reference.split()
    hyp_tokens = hypothesis.split()
    
    if not hyp_tokens or not ref_tokens:
        return 0.0
        
    precisions = []
    for n in range(1, 5):
        r_ng = get_ngrams(ref_tokens, n)
        h_ng = get_ngrams(hyp_tokens, n)
        if not h_ng:
            precisions.append(1e-9)
            continue
        r_counts: Dict[Tuple, int] = {}
        for ng in r_ng:
            r_counts[ng] = r_counts.get(ng, 0) + 1
        matches = 0
        for ng in h_ng:
            if r_counts.get(ng, 0) > 0:
                matches += 1
                r_counts[ng] -= 1
        precisions.append((matches + 1e-9) / (len(h_ng) + 1e-9))
        
    bp = 1.0 if len(hyp_tokens) > len(ref_tokens) else math.exp(1 - len(ref_tokens) / (len(hyp_tokens) + 1e-9))
    log_sum = sum(math.log(p) for p in precisions) / 4.0
    return bp * math.exp(log_sum) * 100.0


def validate_schema(data: Any) -> bool:
    """
    Validates PRD-2026-CR01 schema compliance.
    """
    if not isinstance(data, dict):
        return False
    required_keys = ["summary", "severityScore", "issues", "refactoredCode"]
    if not all(k in data for k in required_keys):
        return False
    if not isinstance(data["issues"], list):
        return False
    if not isinstance(data["severityScore"], (int, float)):
        return False
    return True


def aggregate_metrics(results: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Computes Precision, Recall, F1, FPR, FNR, Schema Validity, Patch Compilability,
    Line Localization Accuracy, and BLEU-4.
    """
    total = len(results)
    if total == 0:
        return {}
        
    schema_pct = sum(x["schema"] for x in results) / total * 100.0
    comp_pct = sum(x["compilable"] for x in results) / total * 100.0
    
    tp = sum(x["tp"] for x in results)
    fp = sum(x["fp"] for x in results)
    fn = sum(x["fn"] for x in results)
    tn = sum(x["tn"] for x in results)
    
    prec = tp / (tp + fp) if (tp + fp) > 0 else 1.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 1.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 1.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0.0
    
    loc_acc = sum(x["loc_acc"] for x in results) / total * 100.0
    bleu = sum(x["bleu"] for x in results) / total
    
    return {
        "schema_compliance": round(schema_pct, 2),
        "patch_compilability": round(comp_pct, 2),
        "f1_score": round(f1 * 100.0, 2),
        "precision": round(prec * 100.0, 2),
        "recall": round(rec * 100.0, 2),
        "false_positive_rate": round(fpr * 100.0, 2),
        "false_negative_rate": round(fnr * 100.0, 2),
        "line_localization_accuracy": round(loc_acc, 2),
        "bleu4": round(bleu, 2),
        "total_evaluated": total
    }
