import json, sys

path10 = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\Completed_Notebook\codedebugger10.ipynb'
path14 = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\NoteBook\codedebugger14.ipynb'

with open(path10, 'r', encoding='utf-8') as f:
    nb10 = json.load(f)

with open(path14, 'r', encoding='utf-8') as f:
    nb14 = json.load(f)

def clean(s):
    return s.encode('ascii', 'replace').decode('ascii')

print('=== NOTEBOOK 10 ===')
print('Total cells:', len(nb10['cells']))
for i, c in enumerate(nb10['cells']):
    src = ''.join(c.get('source', []))
    lines = src.splitlines()
    first_line = clean(lines[0]) if lines else ''
    if c['cell_type'] == 'code' or 'Phase' in first_line or '#' in first_line:
        print(f"Cell {i+1} [{c['cell_type']}]: {first_line[:75]}")

print('\n=== NOTEBOOK 14 ===')
print('Total cells:', len(nb14['cells']))
for i, c in enumerate(nb14['cells']):
    src = ''.join(c.get('source', []))
    lines = src.splitlines()
    first_line = clean(lines[0]) if lines else ''
    if c['cell_type'] == 'code' or 'Phase' in first_line or '#' in first_line:
        print(f"Cell {i+1} [{c['cell_type']}]: {first_line[:75]}")
