import json
import ast
import sys
sys.stdout.reconfigure(encoding='utf-8')

nb_path = r'd:\Engineering\CDAC_ALL_MODULES\Project_CDAC\NoteBook\codedebugger16\codedebugger16.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
md_cells = [c for c in nb['cells'] if c['cell_type'] == 'markdown']
print(f"Code cells: {len(code_cells)}, Markdown cells: {len(md_cells)}")

errors = []
code_idx = 0
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        code_idx += 1
        src = "".join(cell['source'])
        # strip ipython magic commands if any (like !pip or %cd)
        lines = src.split('\n')
        clean_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('!') or stripped.startswith('%'):
                clean_lines.append('# ' + line)
            else:
                clean_lines.append(line)
        clean_src = '\n'.join(clean_lines)
        try:
            ast.parse(clean_src)
        except SyntaxError as e:
            errors.append((i, code_idx, str(e)))

if errors:
    print(f"Found {len(errors)} syntax errors:")
    for cell_idx, c_idx, err in errors:
        print(f"Cell index {cell_idx} (Code #{c_idx}): {err}")
    sys.exit(1)
else:
    print("SUCCESS: All code cells passed ast.parse syntax validation!\n")
    print("Notebook Outline:")
    for i, cell in enumerate(nb['cells']):
        first_line = cell['source'][0].strip() if cell['source'] else ''
        ctype = cell['cell_type']
        print(f"[{i:02d}] {ctype:8s} | {first_line[:80]}")
