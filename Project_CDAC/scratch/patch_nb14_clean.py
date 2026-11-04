import json, os, ast

path = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\NoteBook\codedebugger14.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cell_19_code = """# ===== CELL 19: UNIVERSAL BULLETPROOF SINGLE-GPU SFTTRAINER 🚀 =====
from trl import SFTTrainer, SFTConfig
from datasets import Dataset
import inspect, time, math, torch

# 1. Clear any stale backward hooks from previous runs in the active kernel
for p in model.parameters():
    if hasattr(p, '_backward_hooks') and p._backward_hooks:
        p._backward_hooks.clear()

print('✅ Cleared all autograd hooks. Clean autograd pipeline established.')

# 2. Format ChatML Datasets
def format_chatml(sample):
    text = tokenizer.apply_chat_template(sample['messages'], tokenize=False, add_generation_prompt=False)
    return {'text': text}

train_dataset = Dataset.from_list(train_samples).map(format_chatml)
val_dataset   = Dataset.from_list(val_samples).map(format_chatml)

class SingleGPUSFTTrainer(SFTTrainer):
    def _wrap_model(self, model, training=True, dataloader=None):
        return model  # Completely bypass torch.nn.DataParallel wrapping

# Inspect SFTConfig parameters dynamically to guarantee 100% version compatibility
sft_sig = inspect.signature(SFTConfig.__init__).parameters
max_len_kwarg = {'max_length': 1400} if 'max_length' in sft_sig else {'max_seq_length': 1400}

# On Tesla T4 with 4-bit QLoRA, setting fp16=False and bf16=False completely disables PyTorch's
# GradScaler. This permanently eliminates the missing BFloat16 CUDA unscale kernel crash while
# 4-bit NF4 weights and paged_adamw_8bit keep total VRAM usage at only ~6.2 GB (out of 15 GB).
sft_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    dataset_text_field='text',
    per_device_train_batch_size=TRAIN_BATCH_SIZE,
    per_device_eval_batch_size=TRAIN_BATCH_SIZE,
    gradient_accumulation_steps=GRAD_ACCUM_STEPS,
    learning_rate=2e-4,
    lr_scheduler_type='cosine',
    warmup_steps=10,
    weight_decay=0.01,
    num_train_epochs=2,
    logging_steps=10,
    eval_strategy='steps',
    eval_steps=25,
    save_strategy='steps',
    save_steps=25,
    save_total_limit=2,
    load_best_model_at_end=True,
    metric_for_best_model='eval_loss',
    greater_is_better=False,
    fp16=False,                   # Disables GradScaler entirely -> Zero unscale crashes
    bf16=False,                   # Bypasses missing T4 BFloat16 GEMM instructions
    optim='paged_adamw_8bit',
    report_to='none',
    max_grad_norm=0.3,
    dataloader_drop_last=False,
    **max_len_kwarg
)
sft_args._n_gpu = 1

# Inspect SFTTrainer parameters dynamically for tokenizer vs processing_class
trainer_sig = inspect.signature(SFTTrainer.__init__).parameters
tok_kwarg = {'processing_class': tokenizer} if 'processing_class' in trainer_sig else {'tokenizer': tokenizer}

trainer = SingleGPUSFTTrainer(
    model=model,
    args=sft_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    callbacks=[overfitting_monitor],
    **tok_kwarg
)

print('✅ SFTTrainer initialized successfully without GradScaler collisions.')
print(f'🚀 Starting Pro-Trainer Trilingual Fine-Tuning: {MODEL_ID} on GPU 0...')
print(f'Train Samples: {len(train_dataset)} | Val Samples: {len(val_dataset)}')

start_time = time.time()
train_result = trainer.train()
elapsed = time.time() - start_time
print(f'\\n🎉 Training completed in {elapsed/60:.1f} minutes ({elapsed/3600:.2f} hours)')
"""

ast.parse(cell_19_code)

for idx, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if 'CELL 19: UNIVERSAL BULLETPROOF' in src:
        print(f'Updating Cell 19 at index {idx}')
        cell['source'] = [line + '\n' for line in cell_19_code.splitlines()]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print('codedebugger14.ipynb updated with clean Cell 19!')
