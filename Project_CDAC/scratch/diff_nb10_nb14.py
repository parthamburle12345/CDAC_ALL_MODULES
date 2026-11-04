import json

path10 = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\Completed_Notebook\codedebugger10.ipynb'
path14 = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\NoteBook\codedebugger14.ipynb'

nb10 = json.load(open(path10, encoding='utf-8'))
nb14 = json.load(open(path14, encoding='utf-8'))

diff_cells = []
for i in range(len(nb10['cells'])):
    s10 = ''.join(nb10['cells'][i].get('source', []))
    s14 = ''.join(nb14['cells'][i].get('source', []))
    if s10 != s14:
        diff_cells.append(i + 1)

print(f"Total cells: {len(nb10['cells'])}")
print(f"Cells with differences ({len(diff_cells)} cells): {diff_cells}")

for cell_num in [1, 5, 15, 16, 17, 18, 19, 23, 24, 25, 28]:
    idx = cell_num - 1
    s10 = ''.join(nb10['cells'][idx].get('source', []))
    s14 = ''.join(nb14['cells'][idx].get('source', []))
    print(f"\n--- CELL {cell_num} DIFF SUMMARY ---")
    print(f"NB10 length: {len(s10)} chars | NB14 length: {len(s14)} chars")
    # Show first difference or key details
    for line10, line14 in zip(s10.splitlines()[:5], s14.splitlines()[:5]):
        if line10 != line14:
            print(f"  10: {line10[:60]}")
            print(f"  14: {line14[:60]}")
