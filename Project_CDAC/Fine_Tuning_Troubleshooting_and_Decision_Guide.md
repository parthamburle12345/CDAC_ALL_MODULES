# 🛠️ AI Code Review Model: Fine-Tuning Troubleshooting & Decision Guide
## "If THIS Happens ➔ Do THAT" Diagnostic Matrix
### Project: AI-Powered Code Review & Bug Suggestion System | CDAC PGCP-AI

---

## 📑 Quick Navigation Table

| Category | Problem / Observation | Jump Link |
| :--- | :--- | :--- |
| **Loss & Training** | Loss is flat / does not decrease | [Issue 1](#issue-1-training-loss-is-flat--does-not-decrease) |
| **Loss & Training** | Loss explodes to `NaN` or `Inf` | [Issue 2](#issue-2-training-loss-explodes-to-nan-or-inf) |
| **Generalization** | Validation loss increases while train loss drops (Overfitting) | [Issue 3](#issue-3-validation-loss-increases-while-train-loss-drops-overfitting) |
| **Hardware / VRAM** | `CUDA out of memory` (OOM) on Kaggle A100 | [Issue 4](#issue-4-cuda-out-of-memory-oom-on-gpu) |
| **Hardware / GPU** | GPU Utilization is very low (< 40%) | [Issue 5](#issue-5-gpu-utilization-is-low--3050) |
| **Inference / Schema**| Model outputs conversational text instead of raw JSON | [Issue 6](#issue-6-model-outputs-conversational-chatter-instead-of-strict-json) |
| **Inference / Schema**| Model outputs truncated JSON (missing closing braces) | [Issue 7](#issue-7-model-outputs-truncated-json-missing-closing-brace) |
| **Hallucination** | Model hallucinates invalid C++ syntax or non-existent lines | [Issue 8](#issue-8-model-hallucinates-invalid-line-numbers-or-bugs) |
| **Research Metrics** | CodeBLEU / BLEU is unexpectedly low | [Issue 9](#issue-9-bleu-4-or-codebleu-is-lower-than-expected) |
| **Research Metrics** | Exact Match (EM) is close to 0% | [Issue 10](#issue-10-exact-match-em-is-near-0) |

---

## 1. Training Loss & Optimization Decision Tree

### Issue 1: Training loss is flat / does not decrease
* **Symptom**: Loss starts at ~2.8 and stays between 2.7–2.8 after 100+ steps.
* **Root Causes**:
  1. Learning rate is too low.
  2. LoRA parameters are frozen or not properly registered.
  3. Loss mask is inadvertently masking target tokens.
* **➔ What to Do**:
  1. **Increase Learning Rate**: For LoRA on Qwen2.5-Coder, standard LR is `2e-4`. If you set `1e-5`, it will barely move. Change:
     ```python
     learning_rate = 2e-4  # (or 3e-4)
     ```
  2. **Verify Trainable Parameters**: Verify output of `model.print_trainable_parameters()`. If it shows `trainable%: 0.0000%`, PEFT failed to attach. Ensure `target_modules` contains all linear projection layers:
     ```python
     target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
     ```
  3. **Check Warmup Ratio**: Ensure warmup is 3% (`warmup_ratio=0.03`). If set to 0.5, half the training is at near-zero LR.

---

### Issue 2: Training loss explodes to `NaN` or `Inf`
* **Symptom**: After step 20 or 50, loss suddenly displays `nan`.
* **Root Causes**:
  1. Float16 overflow (fp16 dynamic range is too narrow for deep LLMs).
  2. Learning rate is too high (> 5e-4).
  3. Gradient clipping is missing.
* **➔ What to Do**:
  1. **Switch to Bfloat16**: A100 natively supports `bf16`, which has the exact same dynamic range as `fp32` (8 exponent bits). **Never use `fp16=True` on A100**.
     ```python
     bf16 = True
     fp16 = False
     ```
  2. **Enable Gradient Clipping**: In `TrainingArguments`, set:
     ```python
     max_grad_norm = 1.0
     ```
  3. **Lower Learning Rate**: Reduce LR from `5e-4` to `2e-4` or `1.5e-4`.

---

### Issue 3: Validation loss increases while train loss drops (Overfitting)
* **Symptom**: Training loss drops to 0.3, but Eval loss rises from 0.7 to 1.4.
* **Root Causes**:
  1. Too many epochs for the dataset size.
  2. LoRA rank $r$ is too high for the sample count.
  3. Insufficient data diversity.
* **➔ What to Do**:
  1. **Reduce Epochs / Early Stop**: Stop training after epoch 2 or 3. Code LLMs overfit rapidly on repeated synthetic tokens.
  2. **Increase LoRA Dropout & Weight Decay**:
     ```python
     lora_dropout = 0.1       # Increased from 0.05
     weight_decay = 0.05       # Regularizes optimizer
     ```
  3. **Reduce LoRA Rank**: Drop rank from $r=32$ or $r=64$ down to $r=16$ or $r=8$.

---

## 2. Hardware & Kaggle A100 GPU Optimization

### Issue 4: `CUDA out of memory` (OOM) on GPU
* **Symptom**: PyTorch throws `torch.OutOfMemoryError: CUDA out of memory`.
* **➔ What to Do (Apply in this exact order)**:
  1. **Enable Gradient Checkpointing**: Reduces activation memory by up to 60%:
     ```python
     model.gradient_checkpointing_enable()
     # In TrainingArguments:
     gradient_checkpointing = True
     ```
  2. **Decrease Batch Size & Increase Gradient Accumulation**:
     ```python
     # Old: per_device_batch_size = 8, grad_accum = 2
     # New: per_device_batch_size = 2, grad_accum = 8
     # (Effective batch size remains identical: 2 * 8 = 16, but memory drops 75%!)
     ```
  3. **Limit Max Sequence Length**: Reduce `max_seq_length` from `4096` to `2048` or `1536`.
  4. **Use 4-bit Quantization (QLoRA) if testing on smaller GPUs**:
     ```python
     from transformers import BitsAndBytesConfig
     bnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16)
     ```

---

### Issue 5: GPU Utilization is low (< 30–50%)
* **Symptom**: `nvidia-smi` shows GPU compute at 20–30%, CPU is at 100%. Training is slow.
* **Root Causes**: CPU data loading bottleneck or small batch size starvation.
* **➔ What to Do**:
  1. **Increase DataLoader Workers**:
     ```python
     dataloader_num_workers = 4  # (Kaggle allows up to 4 vCPUs)
     ```
  2. **Pre-tokenize Dataset**: Do not tokenize dynamically during training steps. Pre-tokenize the entire dataset beforehand or use `packing=True` in `SFTTrainer`.
  3. **Enable FlashAttention-2**:
     ```bash
     pip install flash-attn --no-build-isolation
     ```
     ```python
     model = AutoModelForCausalLM.from_pretrained(..., attn_implementation="flash_attention_2")
     ```

---

## 3. Model Output & Schema Reliability

### Issue 6: Model outputs conversational chatter instead of strict JSON
* **Symptom**: Model responds: *"Sure, here is the code review for your file: ```json {...}```"*
* **➔ What to Do**:
  1. **Enforce System Prompt in ChatML**:
     ```json
     {"role": "system", "content": "You are an automated code analyzer. Output ONLY valid JSON conforming to the schema. No markdown formatting, no conversational text."}
     ```
  2. **Lower Generation Temperature**: Set `temperature=0.0` or `0.1` during inference:
     ```python
     outputs = model.generate(..., temperature=0.1, do_sample=False)
     ```
  3. **Regex Extraction in AI Microservice**: In your FastAPI backend, add defensive extraction:
     ```python
     import re, json
     def extract_json(raw):
         match = re.search(r'(\{.*\})', raw, re.DOTALL)
         return json.loads(match.group(1)) if match else None
     ```

---

### Issue 7: Model outputs truncated JSON (missing closing brace)
* **Symptom**: JSON parsing fails with `json.decoder.JSONDecodeError: Expecting ',' or '}'`.
* **Root Causes**: `max_new_tokens` was reached before the model finished writing the JSON findings.
* **➔ What to Do**:
  1. **Increase `max_new_tokens`**:
     ```python
     max_new_tokens = 768  # (or 1024 if file has many findings)
     ```
  2. **Cap Number of Findings**: Instruct the model: *"Report only the top 3 most critical findings."*

---

### Issue 8: Model hallucinates invalid line numbers or bugs
* **Symptom**: Model reports a null pointer bug on line 140, but the file only has 65 lines.
* **Root Causes**: LLM pure text generation lacks real Abstract Syntax Tree (AST) grounding.
* **➔ What to Do (The CDAC Hybrid Architecture Advantage)**:
  1. **Pass AST Metadata in Prompt**: Do not give raw code alone. Prepend line numbers and function boundaries:
     ```text
     [Line 12: void processData(int* ptr)]
     [Line 15: int val = *ptr;]
     ```
  2. **Deterministic Fallback Filter**: Your FastAPI microservice should verify `if finding.line_number > total_lines: drop_finding()`.

---

## 4. Academic Evaluation & Research Paper Ablation Strategy

### Issue 9: BLEU-4 or CodeBLEU is lower than expected
* **Symptom**: BLEU score is only 8.5, and you are worried it's "failing".
* **Academic Reality**:
  * In the **CodeReviewer (EMNLP 2022)** paper (Paper 01 in your `Research/` folder), Microsoft's model achieved:
    * **CodeT5**: BLEU = `2.97`
    * **CodeReviewer**: BLEU = `6.79`
    * **Codex**: BLEU = `8.83`
  * **Why**: Review comments are diverse and non-unique. Two different expert reviewers will write completely different sentences for the exact same bug!
* **➔ What to Do for Your Research Paper**:
  * Do **NOT** rely on standard BLEU alone.
  * Use **CodeBLEU** for the code replacement patches.
  * Use **Semantic Classification F1** (Precision/Recall of Severity and Category).
  * Report **Exact Match (EM)** and **Human/AST Agreement Rate**.

---

### Issue 10: Exact Match (EM) is near 0%
* **Symptom**: EM = 0.00% or 1.2%.
* **Academic Reality**:
  * In Paper 01 (CodeReviewer, Table 6), Exact Match across all state-of-the-art models was **0.00% to 2.1%**.
  * A single space, variable name choice, or comment difference makes EM zero.
* **➔ What to Do**:
  * Report EM alongside normalized AST syntax similarity and CodeBLEU.
  * In your research paper discussion, cite Paper 01: *"As established in Li et al. (EMNLP 2022), raw Exact Match is an overly stringent metric for code refinement due to syntactic variations."*

---

## 5. Recommended Ablation Studies for Your Future Research Paper

To write an IEEE / ACM / Springer-grade research paper from your CDAC project, structure your experimental results around these **4 Ablation Studies**:

```
TABLE 1: Model Variant Comparison (Core Contribution)
┌─────────────────────────────────┬──────────┬──────────┬───────────┬──────────────┐
│ Model / Pipeline Configuration │ BLEU-4   │ CodeBLEU │ Schema %  │ Severity F1  │
├─────────────────────────────────┼──────────┼──────────┼───────────┼──────────────┤
│ 1. Zero-shot Base (Qwen2.5-7B)  │  4.12    │  21.4    │   74.2%   │    0.58      │
│ 2. Few-shot Base + In-Context   │  6.30    │  26.8    │   86.5%   │    0.69      │
│ 3. Static Analysis Alone        │   N/A    │   N/A    │  100.0%   │    0.72      │
│ 4. Fine-Tuned LoRA (Ours)       │  9.45    │  38.2    │   98.8%   │    0.89      │
│ 5. Hybrid (Static + LoRA) [Ours]│ 10.15    │  42.6    │  100.0%   │    0.93      │
└─────────────────────────────────┴──────────┴──────────┴───────────┴──────────────┘
```

1. **Ablation 1 (LoRA Rank Sensitivity)**: Compare $r=8$ vs $r=16$ vs $r=32$. Shows you systematically tuned the model.
2. **Ablation 2 (Context Window Impact)**: Compare 1024 vs 2048 vs 4096 tokens.
3. **Ablation 3 (Hybrid Integration)**: Prove that combining Semgrep static analysis with the Fine-Tuned LLM reduces false positives (aligns with Paper 05 - Tencent).
4. **Ablation 4 (Cross-Language Transfer)**: Evaluate C++ model on Java and Python to demonstrate cross-language code reasoning.
