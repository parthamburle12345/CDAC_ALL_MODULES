import json

path10 = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\Completed_Notebook\codedebugger10.ipynb'
path14 = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\NoteBook\codedebugger14.ipynb'

nb10 = json.load(open(path10, encoding='utf-8'))
nb14 = json.load(open(path14, encoding='utf-8'))

def clean(s):
    return s.encode('ascii', 'replace').decode('ascii')

key_cells = {
    5: "Cell 3 (Runtime 4-bit check & Batch/GradAccum)",
    15: "Cell 10 (C++ Taxonomy)",
    16: "Cell 11 (Java Taxonomy)",
    17: "Cell 12 (Python Taxonomy)",
    18: "Cell 13 (Dataset Synthesis)",
    23: "Cell 17 (LoRA Configuration)",
    24: "Cell 18 (TrainingArguments)",
    25: "Cell 19 (SFTTrainer & Execution)",
    28: "Cell 21 (LoRA Adapter Save)",
    30: "Cell 23 (Benchmark Evaluation)"
}

for idx, title in key_cells.items():
    s10 = clean(''.join(nb10['cells'][idx].get('source', [])))
    s14 = clean(''.join(nb14['cells'][idx].get('source', [])))
    print(f"\n==================== {title} (Index {idx}) ====================")
    print("--- [NB10 Snippet] ---")
    for line in s10.splitlines()[:8]:
        print("  ", line)
    print("--- [NB14 Snippet] ---")
    for line in s14.splitlines()[:8]:
        print("  ", line)
