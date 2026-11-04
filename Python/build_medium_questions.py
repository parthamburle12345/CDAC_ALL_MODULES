# build_medium_questions.py
import json

questions = [
    # Day 01 - 02: Tricky Syntax, Operators, Short-Circuit, Strings (Q101 - Q115)
    {
        "id": 101,
        "topic": "Day 01: Short-Circuit Evaluation",
        "question": "What is the output of the following Python code demonstrating short-circuit evaluation?",
        "code": 'a = "" or "Python"\nb = 0 and 100\nc = [1, 2] or []\nprint(a, b, c)',
        "options": [
            "A) True False True",
            "B) Python 0 [1, 2]",
            "C) Python 100 [1, 2]",
            "D) \"\" 0 []"
        ],
        "answer": "B",
        "explanation": "'or' returns the first truthy operand ('Python') or the last operand. 'and' returns the first falsy operand (0) or the last operand. [1, 2] is truthy, so c is [1, 2]."
    },
    {
        "id": 102,
        "topic": "Day 02: Negative Stride Slicing",
        "question": "Given the string text = 'PYTHON', what is the output of print(text[4:1:-1])?",
        "code": 'text = "PYTHON"\nprint(text[4:1:-1])',
        "options": [
            "A) OHT",
            "B) OHTY",
            "C) NOH",
            "D) THO"
        ],
        "answer": "A",
        "explanation": "text[4] is 'O', text[3] is 'H', text[2] is 'T'. Stop index 1 ('Y') is exclusive. With step -1, it outputs 'OHT'."
    },
    {
        "id": 103,
        "topic": "Day 02: String Immutability in Pipelines",
        "question": "What is the output of the following Python code demonstrating string immutability?",
        "code": 's = "python programming"\ns.upper()\ns.replace("programming", "development")\nres = s.title()\nprint(res)',
        "options": [
            "A) PYTHON DEVELOPMENT",
            "B) Python Development",
            "C) Python Programming",
            "D) PYTHON PROGRAMMING"
        ],
        "answer": "C",
        "explanation": "Because strings are immutable, s.upper() and s.replace() return new strings without modifying s. s remains 'python programming'. Calling s.title() results in 'Python Programming'."
    },
    {
        "id": 104,
        "topic": "Day 01: Loop Else with Break",
        "question": "What is the output of the following loop construct?",
        "code": 'for n in range(2, 6):\n    if n % 4 == 0:\n        print("Found", n)\n        break\nelse:\n    print("Not found")',
        "options": [
            "A) Found 4\\nNot found",
            "B) Found 4",
            "C) Not found",
            "D) Found 2"
        ],
        "answer": "B",
        "explanation": "When n = 4, the condition is met and break is executed. When a loop is exited via break, its else clause is skipped."
    },
    {
        "id": 105,
        "topic": "Day 01: Chained Comparison Operators",
        "question": "What does Python evaluate the chained expression 1 < 3 > 2 == 2 to?",
        "code": 'res = 1 < 3 > 2 == 2\nprint(res)',
        "options": [
            "A) True",
            "B) False",
            "C) TypeError",
            "D) 2"
        ],
        "answer": "A",
        "explanation": "Python evaluates chained comparisons as: (1 < 3) and (3 > 2) and (2 == 2). All three are True, so the result is True."
    },
    {
        "id": 106,
        "topic": "Day 01: Bitwise Shift Operations",
        "question": "What is the result of evaluating (8 >> 2) + (3 << 2) in Python?",
        "code": None,
        "options": [
            "A) 14",
            "B) 16",
            "C) 12",
            "D) 10"
        ],
        "answer": "A",
        "explanation": "8 >> 2 shifts right by 2 bits: 8 // 4 = 2. 3 << 2 shifts left by 2 bits: 3 * 4 = 12. 2 + 12 = 14."
    },
    {
        "id": 107,
        "topic": "Day 02: String find() with Start Index",
        "question": "What is the output of the following string find method call?",
        "code": 'text = "abracadabra"\nprint(text.find("a", 4))',
        "options": [
            "A) 0",
            "B) 3",
            "C) 5",
            "D) 7"
        ],
        "answer": "C",
        "explanation": "find(sub, start) begins searching at index 4 ('c'). The next 'a' occurs at index 5 ('abra[c]a...')."
    },
    {
        "id": 108,
        "topic": "Day 02: String split() with maxsplit",
        "question": "What is the output of 'a:b:c:d'.split(':', 2)?",
        "code": None,
        "options": [
            "A) ['a', 'b', 'c:d']",
            "B) ['a', 'b', 'c', 'd']",
            "C) ['a:b', 'c:d']",
            "D) ['a', 'b:c:d']"
        ],
        "answer": "A",
        "explanation": "maxsplit=2 performs at most 2 splits, yielding a list with 3 elements: ['a', 'b', 'c:d']."
    },
    {
        "id": 109,
        "topic": "Day 02: String Stripping with Specific Characters",
        "question": "What is the output of 'www.cdac.in'.strip('wn.')?",
        "code": None,
        "options": [
            "A) 'cdac'",
            "B) 'www.cdac.i'",
            "C) '.cdac.'",
            "D) 'cdac.in'"
        ],
        "answer": "A",
        "explanation": "strip('wn.') removes any characters from the set {'w', 'n', '.'} from both ends. 'www.' is stripped from left, '.in' is stripped from right, leaving 'cdac'."
    },
    {
        "id": 110,
        "topic": "Day 01: Integer Caching / Small Integer Interning",
        "question": "What is the output of the following comparison demonstrating integer caching in CPython?",
        "code": 'x = 256\ny = 256\na = 257\nb = 257\nprint(x is y, a == b)',
        "options": [
            "A) True True",
            "B) False True",
            "C) True False",
            "D) False False"
        ],
        "answer": "A",
        "explanation": "CPython pre-allocates integers from -5 to 256, so x is y is True. a == b compares values (257 == 257), which is always True."
    },
    {
        "id": 111,
        "topic": "Day 02: String zfill and rjust",
        "question": "What is the output of '42'.zfill(5)?",
        "code": None,
        "options": [
            "A) '42000'",
            "B) '00042'",
            "C) '42.000'",
            "D) '0042'"
        ],
        "answer": "B",
        "explanation": "zfill(width) pads the string on the left with ASCII '0' digits until the given width is reached: '00042'."
    },
    {
        "id": 112,
        "topic": "Day 01: Operator Precedence",
        "question": "What is the output of 3 + 4 * 2 > 10 and not 2 == 3?",
        "code": None,
        "options": [
            "A) False",
            "B) True",
            "C) 11",
            "D) None"
        ],
        "answer": "B",
        "explanation": "4 * 2 = 8; 3 + 8 = 11; 11 > 10 is True. 2 == 3 is False; not False is True. True and True is True."
    },
    {
        "id": 113,
        "topic": "Day 02: f-string Expression Specifier",
        "question": "What does the f-string debugging syntax f'{x=}' output when x = 10?",
        "code": 'x = 10\nprint(f"{x=}")',
        "options": [
            "A) 10",
            "B) x=10",
            "C) {x=10}",
            "D) SyntaxError"
        ],
        "answer": "B",
        "explanation": "Python 3.8+ introduced the '=' specifier in f-strings for self-documenting expressions, producing 'x=10'."
    },
    {
        "id": 114,
        "topic": "Day 01: While Loop Decrement",
        "question": "What does the following while loop print?",
        "code": 'i = 3\nwhile i > 0:\n    i -= 1\n    print(i, end=" ")',
        "options": [
            "A) 3 2 1",
            "B) 2 1 0",
            "C) 3 2 1 0",
            "D) 2 1"
        ],
        "answer": "B",
        "explanation": "Initially i=3; first iteration decrements to 2 (prints 2); second iteration decrements to 1 (prints 1); third decrements to 0 (prints 0). Then i > 0 fails. Output: 2 1 0."
    },
    {
        "id": 115,
        "topic": "Day 02: String partition()",
        "question": "What is the output of 'student@cdac.in'.partition('@')?",
        "code": None,
        "options": [
            "A) ['student', 'cdac.in']",
            "B) ('student', '@', 'cdac.in')",
            "C) ('student', 'cdac.in')",
            "D) 'student'"
        ],
        "answer": "B",
        "explanation": "str.partition(sep) splits at the first occurrence of sep and returns a 3-tuple: (before, sep, after)."
    },

    # Day 03 - 04: Lists, Tuples, Dictionaries, Sets (Q116 - Q135)
    {
        "id": 116,
        "topic": "Day 03: Shallow Copy Mechanics",
        "question": "Consider the following Python code:\na = [[1, 2], [3, 4]]\nb = a.copy()\nb[0][1] = 99\nb.append([5, 6])\nprint(len(a), a[0][1])\nWhat is the output?",
        "code": 'a = [[1, 2], [3, 4]]\nb = a.copy()\nb[0][1] = 99\nb.append([5, 6])\nprint(len(a), a[0][1])',
        "options": [
            "A) 2 99",
            "B) 3 99",
            "C) 2 2",
            "D) 3 2"
        ],
        "answer": "A",
        "explanation": "a.copy() creates a shallow copy. The outer list b has len=3 after append, but a still has len=2. However, inner lists are shared references, so mutating b[0][1] mutates a[0][1] to 99."
    },
    {
        "id": 117,
        "topic": "Day 03: Nested List Comprehension",
        "question": "What is the output of the following nested list comprehension?",
        "code": 'matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nevens = [x for row in matrix for x in row if x % 2 == 0]\nprint(evens)',
        "options": [
            "A) [[2], [4, 6], [8]]",
            "B) [2, 4, 6, 8]",
            "C) [4, 6, 8]",
            "D) [1, 3, 5, 7, 9]"
        ],
        "answer": "B",
        "explanation": "The order of for-clauses matches standard nested loops: for row in matrix: for x in row: if x % 2 == 0. Even elements extracted are [2, 4, 6, 8]."
    },
    {
        "id": 118,
        "topic": "Day 03: List Multiplication Pitfall",
        "question": "What is the output of the following code creating a 2D list via list multiplication?",
        "code": 'grid = [[0] * 2] * 2\ngrid[0][0] = 5\nprint(grid)',
        "options": [
            "A) [[5, 0], [0, 0]]",
            "B) [[5, 0], [5, 0]]",
            "C) [[5, 5], [5, 5]]",
            "D) [[0, 5], [0, 5]]"
        ],
        "answer": "B",
        "explanation": "Multiplying [[0] * 2] * 2 duplicates the reference to the same inner list. Mutating grid[0][0] reflects in both rows: [[5, 0], [5, 0]]."
    },
    {
        "id": 119,
        "topic": "Day 04: Dictionary Dynamic Views",
        "question": "Consider the following dictionary code:\ninventory = {'pen': 10, 'notebook': 5}\nkeys = inventory.keys()\ninventory['pencil'] = 8\ninventory.pop('pen')\nprint(list(keys))\nWhat is the output?",
        "code": 'inventory = {"pen": 10, "notebook": 5}\nkeys = inventory.keys()\ninventory["pencil"] = 8\ninventory.pop("pen")\nprint(list(keys))',
        "options": [
            "A) ['pen', 'notebook']",
            "B) ['notebook', 'pencil']",
            "C) ['pen', 'notebook', 'pencil']",
            "D) RuntimeError is raised"
        ],
        "answer": "B",
        "explanation": "In Python 3, dict.keys() returns a dynamic view object that reflects changes to the underlying dictionary immediately. Converting to list after mutations gives ['notebook', 'pencil']."
    },
    {
        "id": 120,
        "topic": "Day 04: dict.setdefault()",
        "question": "What is the output of the following code using dict.setdefault()?",
        "code": 'data = {"a": 1}\nx = data.setdefault("a", 100)\ny = data.setdefault("b", 200)\nprint(x, y, data["b"])',
        "options": [
            "A) 100 200 200",
            "B) 1 200 200",
            "C) 1 200 None",
            "D) KeyError"
        ],
        "answer": "B",
        "explanation": "If the key already exists, setdefault() returns its existing value (1 for 'a'). If missing, it inserts the key with the default value and returns it (200 for 'b')."
    },
    {
        "id": 121,
        "topic": "Day 04: Dictionary Merge / Unpacking",
        "question": "What is the output of merging two dictionaries using the ** unpacking operator?",
        "code": 'd1 = {"x": 1, "y": 2}\nd2 = {"y": 99, "z": 3}\nres = {**d1, **d2}\nprint(res)',
        "options": [
            "A) {'x': 1, 'y': 2, 'z': 3}",
            "B) {'x': 1, 'y': 99, 'z': 3}",
            "C) {'x': 1, 'y': [2, 99], 'z': 3}",
            "D) SyntaxError"
        ],
        "answer": "B",
        "explanation": "In {**d1, **d2}, keys from later dictionaries overwrite keys from earlier ones. 'y' becomes 99."
    },
    {
        "id": 122,
        "topic": "Day 04: Dictionary fromkeys() Pitfall",
        "question": "What is the output of dict.fromkeys(['a', 'b'], []) after modifying one list?",
        "code": 'd = dict.fromkeys(["a", "b"], [])\nd["a"].append(1)\nprint(d)',
        "options": [
            "A) {'a': [1], 'b': []}",
            "B) {'a': [1], 'b': [1]}",
            "C) {'a': [], 'b': []}",
            "D) KeyError"
        ],
        "answer": "B",
        "explanation": "dict.fromkeys(keys, value) associates each key with the exact same default object reference. Appending to d['a'] modifies the shared list for all keys."
    },
    {
        "id": 123,
        "topic": "Day 03: Modifying List During Iteration",
        "question": "What is the output of removing items from a list while iterating over it with a for loop?",
        "code": 'nums = [1, 2, 3, 4, 5]\nfor x in nums:\n    if x % 2 != 0:\n        nums.remove(x)\nprint(nums)',
        "options": [
            "A) [2, 4]",
            "B) [2, 4, 5]",
            "C) [1, 3, 5]",
            "D) []"
        ],
        "answer": "B",
        "explanation": "Modifying a list during iteration shifts the indices of remaining elements. When 1 is removed, 2 moves to index 0 and is skipped on the next step. 3 is removed, 4 is skipped, and 5 is never checked. Result: [2, 4, 5]."
    },
    {
        "id": 124,
        "topic": "Day 03: Tuple with Mutable List",
        "question": "What happens when you append to a list inside a tuple?",
        "code": 't = (1, [2, 3])\nt[1].append(4)\nprint(t)',
        "options": [
            "A) TypeError: 'tuple' object does not support item assignment",
            "B) (1, [2, 3, 4])",
            "C) (1, [2, 3])",
            "D) ValueError"
        ],
        "answer": "B",
        "explanation": "The tuple's structure (references) remains immutable, but the object at t[1] is a mutable list. Calling .append() mutates the list in place without modifying the tuple reference itself."
    },
    {
        "id": 125,
        "topic": "Day 04: Set Symmetric Difference",
        "question": "What is the output of {1, 2, 3} ^ {2, 3, 4} in Python?",
        "code": None,
        "options": [
            "A) {2, 3}",
            "B) {1, 4}",
            "C) {1, 2, 3, 4}",
            "D) set()"
        ],
        "answer": "B",
        "explanation": "The caret operator ^ computes symmetric difference: elements in either set, but not in both. {1, 2, 3} ^ {2, 3, 4} = {1, 4}."
    },
    {
        "id": 126,
        "topic": "Day 03: List Extended Slicing Assignment",
        "question": "What is the output of the following slice assignment?",
        "code": 'nums = [1, 2, 3, 4, 5]\nnums[1:4] = [20, 30]\nprint(nums)',
        "options": [
            "A) [1, 20, 30, 5]",
            "B) [1, [20, 30], 5]",
            "C) [1, 20, 30, 4, 5]",
            "D) ValueError"
        ],
        "answer": "A",
        "explanation": "Slice assignment replaces the slice [1:4] (elements 2, 3, 4) with the elements from [20, 30]. The list becomes [1, 20, 30, 5]."
    },
    {
        "id": 127,
        "topic": "Day 03: list.sort() with Key Function",
        "question": "What is the output of sorting words by length?",
        "code": 'words = ["banana", "pie", "apple"]\nwords.sort(key=len)\nprint(words)',
        "options": [
            "A) ['apple', 'banana', 'pie']",
            "B) ['pie', 'apple', 'banana']",
            "C) ['banana', 'apple', 'pie']",
            "D) ['pie', 'banana', 'apple']"
        ],
        "answer": "B",
        "explanation": "len('pie')=3, len('apple')=5, len('banana')=6. Sorted by length in ascending order: ['pie', 'apple', 'banana']."
    },
    {
        "id": 128,
        "topic": "Day 04: Dictionary Popitem",
        "question": "What does d.popitem() do on a Python 3.7+ dictionary?",
        "code": 'd = {"a": 1, "b": 2, "c": 3}\nitem = d.popitem()\nprint(item)',
        "options": [
            "A) Removes and returns an arbitrary (random) key-value pair",
            "B) Removes and returns the last inserted key-value pair as a tuple ('c', 3)",
            "C) Removes and returns the first inserted pair ('a', 1)",
            "D) Raises TypeError if no arguments are passed"
        ],
        "answer": "B",
        "explanation": "In Python 3.7+, dictionaries preserve insertion order. popitem() removes and returns the last (LIFO) key-value pair as a (key, value) tuple: ('c', 3)."
    },
    {
        "id": 129,
        "topic": "Day 03: list.count() vs in",
        "question": "What is the output of the following list operations?",
        "code": 'nums = [True, 1, 0, False]\nprint(nums.count(1), nums.count(0))',
        "options": [
            "A) 1 1",
            "B) 2 2",
            "C) 1 2",
            "D) 2 1"
        ],
        "answer": "B",
        "explanation": "In Python, bool is a subclass of int: True == 1 and False == 0. nums.count(1) counts True and 1 (total 2); nums.count(0) counts 0 and False (total 2)."
    },
    {
        "id": 130,
        "topic": "Day 04: Set issubset & issuperset",
        "question": "What is the output of {1, 2}.issubset({1, 2, 3}) and {1, 2, 3}.issuperset({1, 2})?",
        "code": None,
        "options": [
            "A) True True",
            "B) True False",
            "C) False True",
            "D) False False"
        ],
        "answer": "A",
        "explanation": "{1, 2} is a subset of {1, 2, 3}, and {1, 2, 3} is a superset of {1, 2}. Both expressions evaluate to True."
    },

    # Day 05: Functions, Scopes, Closures, RegEx (Q131 - Q150)
    {
        "id": 131,
        "topic": "Day 05: Mutable Default Argument Pitfall",
        "question": "Consider the following function defined with a mutable default argument:\ndef append_record(item, registry=[]):\n    registry.append(item)\n    return registry\nlist1 = append_record('CPU')\nlist2 = append_record('GPU', [])\nlist3 = append_record('RAM')\nprint(list1 is list3, list1, list2)\nWhat is the output?",
        "code": 'def append_record(item, registry=[]):\n    registry.append(item)\n    return registry\nlist1 = append_record("CPU")\nlist2 = append_record("GPU", [])\nlist3 = append_record("RAM")\nprint(list1 is list3, list1, list2)',
        "options": [
            "A) False ['CPU'] ['GPU']",
            "B) True ['CPU', 'RAM'] ['GPU']",
            "C) False ['CPU', 'RAM'] ['GPU']",
            "D) True ['CPU'] ['GPU']"
        ],
        "answer": "B",
        "explanation": "Default argument expressions are evaluated once at function definition time. list1 and list3 share the same default list object. list2 was passed an explicit new list []. Output: True ['CPU', 'RAM'] ['GPU']."
    },
    {
        "id": 132,
        "topic": "Day 05: Higher-Order Functions (map + filter)",
        "question": "What is the output of the following Python code utilizing built-in higher-order functions?",
        "code": 'nums = [1, 2, 3, 4, 5, 6]\nres = list(map(lambda x: x * 10, filter(lambda x: x % 2 != 0, nums)))\nprint(res)',
        "options": [
            "A) [20, 40, 60]",
            "B) [10, 30, 50]",
            "C) [10, 20, 30, 40, 50, 60]",
            "D) [1, 3, 5]"
        ],
        "answer": "B",
        "explanation": "filter keeps odd numbers: [1, 3, 5]. map multiplies each by 10: [10, 30, 50]."
    },
    {
        "id": 133,
        "topic": "Day 05: Regular Expressions match vs search",
        "question": "What is the output of the following regular expression matching code?",
        "code": 'import re\ntext = "Order ID: 98452 shipped"\nm1 = re.match(r"\\d+", text)\nm2 = re.search(r"\\d+", text)\nprint(m1 is None, m2.group())',
        "options": [
            "A) False 98452",
            "B) True 98452",
            "C) True Order",
            "D) False Order"
        ],
        "answer": "B",
        "explanation": "re.match() matches only at the beginning of the string ('Order' does not match \\d+), returning None (m1 is None is True). re.search() scans the entire string and finds '98452'."
    },
    {
        "id": 134,
        "topic": "Day 05: Keyword-Only Arguments (*)",
        "question": "In the function definition 'def connect(host, port, *, timeout=30):', how must 'timeout' be passed?",
        "code": None,
        "options": [
            "A) As a positional argument only",
            "B) As either positional or keyword argument",
            "C) Strictly as a keyword argument (e.g. timeout=10)",
            "D) It cannot be passed at all"
        ],
        "answer": "C",
        "explanation": "The bare asterisk * in the parameter list indicates that all subsequent parameters are keyword-only arguments."
    },
    {
        "id": 135,
        "topic": "Day 05: Positional-Only Arguments (/)",
        "question": "What is the purpose of the slash '/' in 'def add(a, b, /, c):'?",
        "code": None,
        "options": [
            "A) Performs division on a and b",
            "B) Specifies that a and b must be passed as positional-only arguments",
            "C) Specifies that c must be passed as positional-only",
            "D) It is a syntax error"
        ],
        "answer": "B",
        "explanation": "In Python 3.8+, parameters before '/' are positional-only. Calling add(a=1, b=2, c=3) raises a TypeError."
    },
    {
        "id": 136,
        "topic": "Day 05: nonlocal Keyword",
        "question": "What is the output of the following nested function with nonlocal?",
        "code": 'def outer():\n    x = 10\n    def inner():\n        nonlocal x\n        x += 5\n    inner()\n    return x\nprint(outer())',
        "options": [
            "A) 10",
            "B) 15",
            "C) UnboundLocalError",
            "D) None"
        ],
        "answer": "B",
        "explanation": "The nonlocal keyword binds x to the nearest enclosing scope (in outer), allowing inner() to modify outer's x to 15."
    },
    {
        "id": 137,
        "topic": "Day 05: functools.reduce()",
        "question": "What is the output of functools.reduce(lambda acc, x: acc * x, [1, 2, 3, 4])?",
        "code": 'from functools import reduce\nres = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])\nprint(res)',
        "options": [
            "A) 10",
            "B) 24",
            "C) 12",
            "D) [1, 2, 6, 24]"
        ],
        "answer": "B",
        "explanation": "reduce applies the function cumulatively: ((1 * 2) * 3) * 4 = 24."
    },
    {
        "id": 138,
        "topic": "Day 05: RegEx Grouping and sub()",
        "question": "What is the output of re.sub(r'(\\d{2})-(\\d{2})', r'\\2/\\1', '10-25')?",
        "code": 'import re\nres = re.sub(r"(\\d{2})-(\\d{2})", r"\\2/\\1", "10-25")\nprint(res)',
        "options": [
            "A) 10/25",
            "B) 25/10",
            "C) 10-25",
            "D) \\2/\\1"
        ],
        "answer": "B",
        "explanation": "\\1 matches '10', \\2 matches '25'. The replacement r'\\2/\\1' swaps them to '25/10'."
    },
    {
        "id": 139,
        "topic": "Day 05: Lambda Sorting by Multiple Keys",
        "question": "What is the output of sorting students by grade ascending, then age descending?",
        "code": 'students = [("Bob", 20, "B"), ("Alice", 22, "A"), ("Charlie", 19, "A")]\nstudents.sort(key=lambda s: (s[2], -s[1]))\nprint([s[0] for s in students])',
        "options": [
            "A) ['Alice', 'Charlie', 'Bob']",
            "B) ['Charlie', 'Alice', 'Bob']",
            "C) ['Bob', 'Alice', 'Charlie']",
            "D) ['Alice', 'Bob', 'Charlie']"
        ],
        "answer": "A",
        "explanation": "Grade 'A' comes before 'B'. For grade 'A', -s[1] sorts age descending: Alice (-22) comes before Charlie (-19). Output: ['Alice', 'Charlie', 'Bob']."
    },
    {
        "id": 140,
        "topic": "Day 05: Unpacking in Function Calls",
        "question": "What is the output of the following function call using * and ** unpacking?",
        "code": 'def display(a, b, c=10):\n    return a + b + c\nargs = (5,)\nkwargs = {"b": 15, "c": 20}\nprint(display(*args, **kwargs))',
        "options": [
            "A) 30",
            "B) 40",
            "C) 50",
            "D) TypeError"
        ],
        "answer": "B",
        "explanation": "display(*args, **kwargs) unpacks a=5, b=15, c=20. 5 + 15 + 20 = 40."
    },
    {
        "id": 141,
        "topic": "Day 05: Recursion Base Case",
        "question": "What happens if a recursive function in Python has no terminating base case?",
        "code": None,
        "options": [
            "A) System crash with Segmentation Fault",
            "B) RecursionError: maximum recursion depth exceeded",
            "C) It loops infinitely without raising any error",
            "D) Returns None automatically"
        ],
        "answer": "B",
        "explanation": "Python has a call stack depth limit (typically 1000). Exceeding it raises a RecursionError."
    },
    {
        "id": 142,
        "topic": "Day 05: RegEx re.split()",
        "question": "What does re.split(r'[,;\\s]+', 'apple, banana; orange grape') produce?",
        "code": None,
        "options": [
            "A) ['apple', 'banana', 'orange', 'grape']",
            "B) ['apple,', 'banana;', 'orange', 'grape']",
            "C) ['apple', '', 'banana', '', 'orange', 'grape']",
            "D) ['apple']"
        ],
        "answer": "A",
        "explanation": "The pattern [,;\\s]+ matches one or more commas, semicolons, or whitespace characters, neatly splitting all words."
    },
    {
        "id": 143,
        "topic": "Day 05: Function Annotation Attributes",
        "question": "Where are function parameter and return type annotations stored at runtime?",
        "code": 'def greet(name: str) -> str:\n    return "Hi " + name',
        "options": [
            "A) greet.__doc__",
            "B) greet.__annotations__",
            "C) greet.__types__",
            "D) greet.__signature__"
        ],
        "answer": "B",
        "explanation": "Function annotations are stored in the function's __annotations__ dictionary attribute."
    },
    {
        "id": 144,
        "topic": "Day 05: Basic Decorator Syntax",
        "question": "What is the equivalent syntax for decorating a function with @my_decorator?",
        "code": '@my_decorator\ndef func(): pass',
        "options": [
            "A) func = my_decorator(func)",
            "B) func = my_decorator()",
            "C) my_decorator = func(my_decorator)",
            "D) my_decorator.call(func)"
        ],
        "answer": "A",
        "explanation": "The @my_decorator syntax is syntactic sugar for reassigning func = my_decorator(func)."
    },
    {
        "id": 145,
        "topic": "Day 05: Scope LEGB Rule",
        "question": "What is the resolution order Python follows when looking up an unqualified variable name?",
        "code": None,
        "options": [
            "A) Global -> Enclosing -> Local -> Built-in",
            "B) Local -> Enclosing -> Global -> Built-in",
            "C) Local -> Global -> Enclosing -> Built-in",
            "D) Built-in -> Global -> Enclosing -> Local"
        ],
        "answer": "B",
        "explanation": "Python resolves variables using LEGB: Local scope first, then Enclosing functions, then Global (module level), then Built-in."
    },

    # Day 06: Object-Oriented Programming (Q146 - Q165)
    {
        "id": 146,
        "topic": "Day 06: Class Attribute Shadowing",
        "question": "Consider the following class definition and attribute assignments:\nclass Device:\n    count = 0\n    def __init__(self, name):\n        self.name = name\n        Device.count += 1\nd1 = Device('Router')\nd2 = Device('Switch')\nd1.count = 10\nprint(d1.count, d2.count, Device.count)\nWhat is the output?",
        "code": 'class Device:\n    count = 0\n    def __init__(self, name):\n        self.name = name\n        Device.count += 1\nd1 = Device("Router")\nd2 = Device("Switch")\nd1.count = 10\nprint(d1.count, d2.count, Device.count)',
        "options": [
            "A) 10 10 10",
            "B) 10 2 2",
            "C) 2 2 2",
            "D) 10 2 10"
        ],
        "answer": "B",
        "explanation": "Device.count is incremented twice (count=2). Assigning d1.count = 10 creates an instance attribute on d1 that shadows the class attribute. d2.count and Device.count still access the class attribute (2)."
    },
    {
        "id": 147,
        "topic": "Day 06: Property Setter with Validation",
        "question": "Consider the following class using a property setter with validation:\nclass Wallet:\n    def __init__(self, balance):\n        self.balance = balance\n    @property\n    def balance(self):\n        return self.__balance\n    @balance.setter\n    def balance(self, amount):\n        if amount < 0:\n            raise ValueError('Negative balance')\n        self.__balance = amount\nw = Wallet(50)\ntry:\n    w.balance -= 100\nexcept ValueError:\n    w.balance += 20\nprint(w.balance)\nWhat is the output?",
        "code": 'class Wallet:\n    def __init__(self, balance):\n        self.balance = balance\n    @property\n    def balance(self):\n        return self.__balance\n    @balance.setter\n    def balance(self, amount):\n        if amount < 0:\n            raise ValueError("Negative balance")\n        self.__balance = amount\nw = Wallet(50)\ntry:\n    w.balance -= 100\nexcept ValueError:\n    w.balance += 20\nprint(w.balance)',
        "options": [
            "A) 70",
            "B) -30",
            "C) 20",
            "D) -50"
        ],
        "answer": "A",
        "explanation": "w.balance -= 100 evaluates to w.balance = 50 - 100 = -50, which raises ValueError in setter before modifying __balance. In the except block, w.balance += 20 modifies 50 to 70. w.balance prints 70."
    },
    {
        "id": 148,
        "topic": "Day 06: Name Mangling for Private Attributes",
        "question": "How does Python mangle a private attribute named '__secret' inside class 'Account'?",
        "code": 'class Account:\n    def __init__(self):\n        self.__secret = 1234',
        "options": [
            "A) It makes it completely inaccessible outside the class",
            "B) It rewrites it internally as _Account__secret",
            "C) It encrypts the variable name using MD5",
            "D) It moves it to __dict__['secret']"
        ],
        "answer": "B",
        "explanation": "Python enforces private variables with leading double underscores via name mangling: _ClassName__var, making it _Account__secret."
    },
    {
        "id": 149,
        "topic": "Day 06: @classmethod vs @staticmethod",
        "question": "What is the fundamental difference in parameter passing between @classmethod and @staticmethod?",
        "code": None,
        "options": [
            "A) @classmethod receives the class object ('cls') as its first parameter; @staticmethod receives neither self nor cls.",
            "B) @classmethod receives 'self', while @staticmethod receives 'cls'.",
            "C) @staticmethod can modify class state, while @classmethod cannot.",
            "D) @classmethod can only be called from an instance."
        ],
        "answer": "A",
        "explanation": "@classmethod receives the class object (cls) as its first implicit parameter. @staticmethod is a plain function scoped inside the class namespace, receiving neither self nor cls."
    },
    {
        "id": 150,
        "topic": "Day 06: Dunder __repr__ vs __str__",
        "question": "When both __str__ and __repr__ are defined in a class, which one does repr() invoke, and which one does str() invoke?",
        "code": None,
        "options": [
            "A) Both invoke __str__",
            "B) repr() invokes __repr__; str() invokes __str__ (falling back to __repr__ if __str__ is missing)",
            "C) repr() invokes __str__; str() invokes __repr__",
            "D) Both invoke __repr__"
        ],
        "answer": "B",
        "explanation": "repr(obj) calls __repr__ (unambiguous developer representation). str(obj) calls __str__ (human-readable string); if __str__ is not implemented, Python falls back to __repr__."
    },
    {
        "id": 151,
        "topic": "Day 06: Dunder __len__ Protocol",
        "question": "What requirement must the return value of __len__() fulfill?",
        "code": None,
        "options": [
            "A) It can return any string or integer",
            "B) It must return a non-negative integer (>= 0)",
            "C) It must return a float",
            "D) It can return negative integers for reverse sequences"
        ],
        "answer": "B",
        "explanation": "Python requires __len__() to return a non-negative integer (>= 0). Returning a negative number or non-integer raises a TypeError or ValueError."
    },
    {
        "id": 152,
        "topic": "Day 06: Operator Overloading (__add__)",
        "question": "What is the output of the following Vector addition code?",
        "code": 'class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nv3 = v1 + v2\nprint(v3.x, v3.y)',
        "options": [
            "A) 1 2",
            "B) 3 4",
            "C) 4 6",
            "D) TypeError"
        ],
        "answer": "C",
        "explanation": "v1 + v2 calls v1.__add__(v2), which adds coordinates: 1+3=4 and 2+4=6. Output: 4 6."
    },
    {
        "id": 153,
        "topic": "Day 06: super() with Single Inheritance",
        "question": "What does super().__init__() do in a child class constructor?",
        "code": 'class A:\n    def __init__(self):\n        self.val = 10\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        self.val += 5\nb = B()\nprint(b.val)',
        "options": [
            "A) 10",
            "B) 15",
            "C) 5",
            "D) AttributeError"
        ],
        "answer": "B",
        "explanation": "super().__init__() calls parent class A's constructor, setting self.val = 10. Then self.val += 5 increases it to 15."
    },
    {
        "id": 154,
        "topic": "Day 06: Dunder __eq__ and Hashability",
        "question": "What happens to a class's default __hash__ when it implements custom __eq__ without defining __hash__?",
        "code": 'class Point:\n    def __init__(self, x):\n        self.x = x\n    def __eq__(self, other):\n        return self.x == other.x',
        "options": [
            "A) __hash__ remains the default object memory hash",
            "B) Python automatically sets __hash__ = None, making instances unhashable",
            "C) Python automatically hashes all instance attributes",
            "D) Point objects can still be used as set elements"
        ],
        "answer": "B",
        "explanation": "In Python 3, defining a custom __eq__ without defining __hash__ sets __hash__ to None, making instances unhashable and raising TypeError if added to a set or dict key."
    },
    {
        "id": 155,
        "topic": "Day 06: Polymorphism and Method Overriding",
        "question": "What is the output of the following polymorphic function call?",
        "code": 'class Dog:\n    def speak(self): return "Woof"\nclass Cat:\n    def speak(self): return "Meow"\ndef animal_sound(sounder):\n    return sounder.speak()\nprint([animal_sound(a) for a in [Dog(), Cat()]])',
        "options": [
            "A) ['Woof', 'Meow']",
            "B) ['Woof', 'Woof']",
            "C) ['Meow', 'Meow']",
            "D) TypeError"
        ],
        "answer": "A",
        "explanation": "Python uses duck typing: as long as each object implements .speak(), the function calls their respective method implementations."
    },

    # Day 07: File Handling, Serialization & SQLite (Q156 - Q175)
    {
        "id": 156,
        "topic": "Day 07: File seek() and tell()",
        "question": "Suppose a text file 'test.txt' contains the 10-character string 'abcdefghij'. What is the output of the following code?",
        "code": 'with open("test.txt", "r", encoding="utf-8") as f:\n    f.seek(4)\n    chunk = f.read(3)\n    pos = f.tell()\n    print(chunk, pos)',
        "options": [
            "A) cde 7",
            "B) def 6",
            "C) efg 7",
            "D) efg 6"
        ],
        "answer": "C",
        "explanation": "seek(4) places the cursor at index 4 (0:'a', 1:'b', 2:'c', 3:'d', 4:'e'). read(3) reads 3 chars: 'efg'. The file pointer is now at index 7. tell() returns 7."
    },
    {
        "id": 157,
        "topic": "Day 07: Pickle File Mode Requirement",
        "question": "When using the pickle module to serialize a Python object directly to a file on disk, in which access mode must the file be opened?",
        "code": None,
        "options": [
            "A) 'w'",
            "B) 'r'",
            "C) 'wb'",
            "D) 'a'"
        ],
        "answer": "C",
        "explanation": "pickle serializes Python objects into a binary byte stream. Thus, the file must be opened in write-binary mode ('wb')."
    },
    {
        "id": 158,
        "topic": "Day 07: csv.DictReader Structure",
        "question": "What does each row produced by csv.DictReader represent?",
        "code": None,
        "options": [
            "A) A tuple of values",
            "B) A list of comma-separated strings",
            "C) A dictionary mapping header column names to row string values",
            "D) A JSON object string"
        ],
        "answer": "C",
        "explanation": "csv.DictReader maps the fieldnames in the first row to each subsequent row's values, returning each row as an OrderedDict/dict."
    },
    {
        "id": 159,
        "topic": "Day 07: json.loads vs json.load",
        "question": "What is the difference between json.loads() and json.load()?",
        "code": None,
        "options": [
            "A) json.loads() parses from a string; json.load() parses from a file-like stream object.",
            "B) json.load() parses from a string; json.loads() parses from a file.",
            "C) json.loads() is for lists only; json.load() is for dicts.",
            "D) They are aliases for each other."
        ],
        "answer": "A",
        "explanation": "json.loads(s) (load string) deserializes a JSON string into a Python object. json.load(fp) deserializes directly from an open file/stream."
    },
    {
        "id": 160,
        "topic": "Day 07: SQLite Parameterized Queries",
        "question": "Why should SQL queries with variables always use parameterized placeholders (e.g., '?') instead of string formatting?",
        "code": 'cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))',
        "options": [
            "A) String formatting is deprecated in Python 3",
            "B) To prevent SQL Injection attacks by letting the DB driver properly escape parameters",
            "C) Parameterized queries run 100x faster",
            "D) SQLite does not support string concatenation"
        ],
        "answer": "B",
        "explanation": "Parameterized queries separate SQL code from untrusted user data, preventing SQL Injection vulnerabilities."
    },
    {
        "id": 161,
        "topic": "Day 07: SQLite commit() Requirement",
        "question": "In Python's sqlite3 module, what happens to INSERT and UPDATE queries if conn.commit() is NOT called before closing the connection?",
        "code": None,
        "options": [
            "A) Changes are committed automatically on close",
            "B) Changes are rolled back and not persisted to disk",
            "C) An OperationalError is raised",
            "D) The database file gets corrupted"
        ],
        "answer": "B",
        "explanation": "By default, sqlite3 starts transactions implicitly. Any uncommitted data modifications (INSERT/UPDATE/DELETE) are rolled back if the connection is closed without calling conn.commit()."
    },
    {
        "id": 162,
        "topic": "Day 07: File 'r+' Mode",
        "question": "What does opening a file with mode 'r+' allow you to do?",
        "code": None,
        "options": [
            "A) Read only, but with root permissions",
            "B) Read and write without truncating existing file contents",
            "C) Write only, creating the file if missing",
            "D) Append only to binary files"
        ],
        "answer": "B",
        "explanation": "'r+' opens an existing file for both reading and writing without truncating it. Writing begins at the current file pointer position."
    },
    {
        "id": 163,
        "topic": "Day 07: File 'w' Truncation",
        "question": "What happens to an existing file when it is opened with mode 'w'?",
        "code": None,
        "options": [
            "A) It appends to the existing file",
            "B) Its existing contents are immediately truncated (erased to 0 bytes)",
            "C) A FileExistsError is raised",
            "D) It opens in read-only mode"
        ],
        "answer": "B",
        "explanation": "Mode 'w' truncates the file immediately upon opening, erasing any existing contents."
    },
    {
        "id": 164,
        "topic": "Day 07: File readline() Trailing Newline",
        "question": "What does f.readline() return when it reads a line from a text file, and how does it signal End of File (EOF)?",
        "code": None,
        "options": [
            "A) Returns a string including the trailing '\\n'; returns '' (empty string) at EOF",
            "B) Strips the newline automatically; returns None at EOF",
            "C) Returns a list of characters; raises EOFError at EOF",
            "D) Returns a byte array; returns -1 at EOF"
        ],
        "answer": "A",
        "explanation": "readline() includes the trailing newline character '\\n' (unless it's the last line without one). It returns an empty string '' when EOF is reached."
    },
    {
        "id": 165,
        "topic": "Day 07: SQLite fetchall() Return Type",
        "question": "What does cursor.fetchall() return after executing a SELECT query in sqlite3?",
        "code": 'cursor.execute("SELECT id, name FROM users")\nrows = cursor.fetchall()',
        "options": [
            "A) A dictionary of rows",
            "B) A list of tuples, where each tuple represents a row",
            "C) A pandas DataFrame",
            "D) A JSON string"
        ],
        "answer": "B",
        "explanation": "By default, cursor.fetchall() returns a list of tuples containing column values."
    },

    # Day 08: Iterators, Generators, Advanced Constructs (Q166 - Q175)
    {
        "id": 166,
        "topic": "Day 08: Generator Function Invocation",
        "question": "In Python, what occurs when a generator function containing the yield statement is called?",
        "code": 'def my_gen():\n    print("Starting")\n    yield 1\ng = my_gen()',
        "options": [
            "A) It executes the function body to completion and returns a tuple of results",
            "B) It immediately returns a generator iterator object without executing the function body",
            "C) It executes up to the first yield statement and prints 'Starting'",
            "D) It raises a SyntaxError if it does not also include a return statement"
        ],
        "answer": "B",
        "explanation": "Calling a generator function returns a generator object without executing any code inside the function until next() or a loop is invoked."
    },
    {
        "id": 167,
        "topic": "Day 08: Generator next() and StopIteration",
        "question": "What is the output of the following generator code?",
        "code": 'def count_up():\n    yield 1\n    yield 2\nc = count_up()\nprint(next(c), next(c))\ntry:\n    next(c)\nexcept StopIteration:\n    print("Done")',
        "options": [
            "A) 1 2\\nDone",
            "B) 1 2\\nNone",
            "C) 1 2\\nStopIteration",
            "D) 1 1\\nDone"
        ],
        "answer": "A",
        "explanation": "The generator yields 1, then 2. The third call to next(c) exhausts the generator, raising StopIteration, caught to print 'Done'."
    },
    {
        "id": 168,
        "topic": "Day 08: Custom Iterator Protocol",
        "question": "Which two special methods must an object implement to satisfy the Python Iterator Protocol?",
        "code": None,
        "options": [
            "A) __init__ and __del__",
            "B) __iter__ and __next__",
            "C) __enter__ and __exit__",
            "D) __len__ and __getitem__"
        ],
        "answer": "B",
        "explanation": "The iterator protocol requires __iter__() (returning self) and __next__() (returning the next item or raising StopIteration)."
    },
    {
        "id": 169,
        "topic": "Day 08: Generator Expression Memory Efficiency",
        "question": "What is the primary architectural advantage of a generator expression over a list comprehension?",
        "code": 'gen = (x * 2 for x in range(1_000_000))\nlst = [x * 2 for x in range(1_000_000)]',
        "options": [
            "A) Generator expressions execute twice as fast.",
            "B) Generator expressions evaluate lazily one item at a time, using O(1) constant memory instead of allocating a large list in RAM.",
            "C) Generator expressions can be indexed with square brackets gen[0].",
            "D) Generator expressions can be iterated over multiple times."
        ],
        "answer": "B",
        "explanation": "Generator expressions produce items on-demand (lazy evaluation), maintaining a minimal memory footprint."
    },
    {
        "id": 170,
        "topic": "Day 08: itertools.chain()",
        "question": "What is the output of list(itertools.chain([1, 2], ['a', 'b']))?",
        "code": 'import itertools\nres = list(itertools.chain([1, 2], ["a", "b"]))\nprint(res)',
        "options": [
            "A) [[1, 2], ['a', 'b']]",
            "B) [1, 2, 'a', 'b']",
            "C) [(1, 'a'), (2, 'b')]",
            "D) {'1': 'a', '2': 'b'}"
        ],
        "answer": "B",
        "explanation": "itertools.chain() links multiple iterables consecutively into a single sequence: [1, 2, 'a', 'b']."
    },
    {
        "id": 171,
        "topic": "Day 08: yield from Syntax",
        "question": "What does 'yield from sub_iterable' do inside a generator function?",
        "code": 'def combo():\n    yield from [10, 20]\n    yield 30',
        "options": [
            "A) Yields the list [10, 20] as a single entity",
            "B) Delegates iteration to sub_iterable, yielding each of its items transparently",
            "C) Imports a generator from another file",
            "D) Terminates the generator"
        ],
        "answer": "B",
        "explanation": "yield from delegates iteration to a sub-generator or iterable, yielding each element individually (10, then 20, then 30)."
    },
    {
        "id": 172,
        "topic": "Day 08: Built-in iter() with Sentinel",
        "question": "What does the two-argument form iter(callable, sentinel) do?",
        "code": None,
        "options": [
            "A) Iterates over sentinel using callable",
            "B) Repeatedly calls callable with no arguments until it returns sentinel, then stops",
            "C) Raises TypeError because iter takes 1 argument",
            "D) Creates a circular iterator"
        ],
        "answer": "B",
        "explanation": "iter(callable, sentinel) creates an iterator that invokes callable on each next() call until the returned value equals sentinel."
    },
    {
        "id": 173,
        "topic": "Day 08: Generator State Persistence",
        "question": "What is the output of the following generator function?",
        "code": 'def tracker():\n    count = 0\n    while True:\n        count += 1\n        yield count\nt = tracker()\nprint(next(t), next(t), next(t))',
        "options": [
            "A) 1 1 1",
            "B) 1 2 3",
            "C) 0 1 2",
            "D) Infinite loop"
        ],
        "answer": "B",
        "explanation": "Generators freeze and maintain their local stack frame between yield statements. count increments on each resumption: 1, 2, 3."
    },
    {
        "id": 174,
        "topic": "Day 08: Exception Handling (try-except-else-finally)",
        "question": "Consider the following function with try-except-finally return values:\ndef calculate_status(val):\n    try:\n        if val < 0:\n            raise ValueError('Invalid number')\n        return 'PROCESSED'\n    except ValueError:\n        return 'CAUGHT_ERROR'\n    finally:\n        return 'CLEANUP_DONE'\nprint(calculate_status(-5), calculate_status(10))\nWhat is the output?",
        "code": 'def calculate_status(val):\n    try:\n        if val < 0:\n            raise ValueError("Invalid number")\n        return "PROCESSED"\n    except ValueError:\n        return "CAUGHT_ERROR"\n    finally:\n        return "CLEANUP_DONE"\nprint(calculate_status(-5), calculate_status(10))',
        "options": [
            "A) CAUGHT_ERROR PROCESSED",
            "B) CLEANUP_DONE CLEANUP_DONE",
            "C) CAUGHT_ERROR CLEANUP_DONE",
            "D) CLEANUP_DONE PROCESSED"
        ],
        "answer": "B",
        "explanation": "A return statement in a finally block always overrides any return statement executed in the try or except blocks. Both calls return 'CLEANUP_DONE'."
    },
    {
        "id": 175,
        "topic": "Day 08: Try-Except-Else Block",
        "question": "When does the else block of a try-except statement execute?",
        "code": 'try:\n    x = 10 / 2\nexcept ZeroDivisionError:\n    print("Error")\nelse:\n    print("Success")\nfinally:\n    print("Done")',
        "options": [
            "A) Only if an exception was raised and caught",
            "B) Only if NO exception was raised in the try block",
            "C) Always, before the finally block",
            "D) Never"
        ],
        "answer": "B",
        "explanation": "The else block of a try statement executes only if the try clause finishes without raising any exception."
    },

    # Day 09 - 10: Web Frameworks, APIs & Scraping (Q176 - Q190)
    {
        "id": 176,
        "topic": "Day 09: Flask Route Dynamic Parameters",
        "question": "In Flask, how do you define a route variable rule that accepts only integers as book_id?",
        "code": None,
        "options": [
            "A) @app.route('/books/<int:book_id>')",
            "B) @app.route('/books/<book_id:int>')",
            "C) @app.route('/books/{int book_id}')",
            "D) @app.route('/books/%d')"
        ],
        "answer": "A",
        "explanation": "Flask uses angle brackets with type converters: @app.route('/books/<int:book_id>')."
    },
    {
        "id": 177,
        "topic": "Day 09: Flask HTTP Methods Configuration",
        "question": "By default, which HTTP methods does a Flask route handler accept if the methods argument is omitted?",
        "code": '@app.route("/items")\ndef get_items(): pass',
        "options": [
            "A) GET and POST",
            "B) GET only",
            "C) ALL HTTP methods",
            "D) POST only"
        ],
        "answer": "B",
        "explanation": "By default, Flask routes listen only to GET requests (and implicitly HEAD/OPTIONS). To accept POST, methods=['GET', 'POST'] must be declared."
    },
    {
        "id": 178,
        "topic": "Day 09: MVC vs MVT Pattern",
        "question": "In Django's Model-View-Template (MVT) architecture, which component corresponds to the Controller in the classic MVC design pattern?",
        "code": None,
        "options": [
            "A) Model (models.py)",
            "B) View (views.py)",
            "C) Template (templates/*.html)",
            "D) Dispatcher (urls.py)"
        ],
        "answer": "B",
        "explanation": "In Django MVT, the View (views.py) contains business logic and controls data flow, corresponding to the Controller in MVC. The Template corresponds to the View."
    },
    {
        "id": 179,
        "topic": "Day 10: BeautifulSoup Scraping Tag & Attribute",
        "question": "Consider the following BeautifulSoup web scraping code:\nfrom bs4 import BeautifulSoup\nhtml = '<a href=\"https://example.com\" class=\"link-btn\">Click Here</a>'\nsoup = BeautifulSoup(html, 'html.parser')\ntag = soup.find('a')\nprint(tag.text, tag['href'])\nWhat is the output?",
        "code": 'from bs4 import BeautifulSoup\nhtml = \'<a href="https://example.com" class="link-btn">Click Here</a>\'\nsoup = BeautifulSoup(html, "html.parser")\ntag = soup.find("a")\nprint(tag.text, tag["href"])',
        "options": [
            "A) Click Here https://example.com",
            "B) Click Here link-btn",
            "C) <a href=\"https://example.com\"> Click Here",
            "D) link-btn https://example.com"
        ],
        "answer": "A",
        "explanation": "tag.text extracts the visible inner text ('Click Here'), and tag['href'] accesses the HTML attribute value ('https://example.com')."
    },
    {
        "id": 180,
        "topic": "Day 10: REST API Status Code 204",
        "question": "What does HTTP status code 204 No Content indicate in a REST API?",
        "code": None,
        "options": [
            "A) The requested resource could not be found",
            "B) The server successfully processed the request, but is not returning any content in the response body (common for DELETE operations)",
            "C) The client sent an empty request body",
            "D) The server encountered an internal error"
        ],
        "answer": "B",
        "explanation": "204 No Content signifies that the action was successfully fulfilled, but there is no payload body to return (standard for successful DELETE)."
    },
    {
        "id": 181,
        "topic": "Day 10: HTTP Verbs Idempotency",
        "question": "Which of the following HTTP methods is NOT idempotent according to REST conventions?",
        "code": None,
        "options": [
            "A) GET",
            "B) PUT",
            "C) DELETE",
            "D) POST"
        ],
        "answer": "D",
        "explanation": "An idempotent method produces the same result on multiple identical requests. GET, PUT, and DELETE are idempotent. POST creates new resources on each call and is non-idempotent."
    },
    {
        "id": 182,
        "topic": "Day 10: Flask request.get_json()",
        "question": "In a Flask REST API view, what does request.get_json() return when incoming request has 'Content-Type: application/json'?",
        "code": '@app.route("/api/users", methods=["POST"])\ndef add_user():\n    data = request.get_json()',
        "options": [
            "A) A raw JSON string",
            "B) A parsed Python dictionary or list",
            "C) A Werkzeug Response object",
            "D) An XML tree"
        ],
        "answer": "B",
        "explanation": "request.get_json() parses the incoming JSON request payload into a native Python dictionary or list."
    },
    {
        "id": 183,
        "topic": "Day 10: BeautifulSoup find_all()",
        "question": "What does soup.find_all('p', class_='intro') return?",
        "code": None,
        "options": [
            "A) The first matching <p> tag",
            "B) A list of all matching <p> tag elements with class 'intro'",
            "C) A dictionary of text contents",
            "D) A string containing concatenated paragraphs"
        ],
        "answer": "B",
        "explanation": "find_all() returns a list of all matching Tag objects matching the tag name and attributes."
    },
    {
        "id": 184,
        "topic": "Day 10: Flask jsonify() Helper",
        "question": "What are the two primary things Flask's jsonify({'key': 'val'}) does?",
        "code": None,
        "options": [
            "A) Serializes data to JSON and sets Content-Type header to 'application/json'",
            "B) Compresses JSON with gzip and saves to disk",
            "C) Validates JSON schema against SQLite database",
            "D) Converts dict to HTML table"
        ],
        "answer": "A",
        "explanation": "jsonify() serializes the Python object into JSON format and sets the HTTP response mimetype header to 'application/json'."
    },
    {
        "id": 185,
        "topic": "Day 10: HTTP 405 Status Code",
        "question": "When does Flask return HTTP status code 405 Method Not Allowed?",
        "code": None,
        "options": [
            "A) When an invalid URL route is requested",
            "B) When a client attempts an HTTP method (e.g. POST) not registered in the route's methods list",
            "C) When authentication credentials are missing",
            "D) When server encounters an uncaught exception"
        ],
        "answer": "B",
        "explanation": "405 Method Not Allowed indicates the resource exists, but does not support the HTTP verb used by the client."
    },

    # Day 10 - 11: NumPy & Pandas Foundations (Q186 - Q200)
    {
        "id": 186,
        "topic": "Day 10: NumPy 2D Array Slicing",
        "question": "Given arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), what is arr[:2, 1:]?",
        "code": 'import numpy as np\narr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])\nsub = arr[:2, 1:]\nprint(sub)',
        "options": [
            "A) [[20, 30], [50, 60]]",
            "B) [[10, 20], [40, 50]]",
            "C) [[50, 60], [80, 90]]",
            "D) [[20, 50], [30, 60]]"
        ],
        "answer": "A",
        "explanation": "arr[:2, 1:] slices rows 0 and 1, and columns from index 1 onward (columns 1 and 2), giving [[20, 30], [50, 60]]."
    },
    {
        "id": 187,
        "topic": "Day 10: NumPy reshape() with -1",
        "question": "What is the resulting shape when arr = np.arange(12).reshape((3, -1)) is executed?",
        "code": 'import numpy as np\narr = np.arange(12).reshape((3, -1))\nprint(arr.shape)',
        "options": [
            "A) (3, 4)",
            "B) (4, 3)",
            "C) (3, 12)",
            "D) ValueError"
        ],
        "answer": "A",
        "explanation": "Passing -1 to reshape tells NumPy to infer that dimension automatically: 12 / 3 = 4 columns. Shape is (3, 4)."
    },
    {
        "id": 188,
        "topic": "Day 11: Pandas Boolean Filtering Syntax",
        "question": "In Pandas, why does executing df[df['Units'] > 2 and df['Price'] < 20] raise a ValueError, and what is the required syntax?",
        "code": None,
        "options": [
            "A) Column names must be prefixed with index; syntax must use df.query_filter()",
            "B) Python's 'and' operator evaluates the truth value of the entire Series as ambiguous; the bitwise operator '&' with parentheses df[(df['Units'] > 2) & (df['Price'] < 20)] must be used",
            "C) Pandas does not support multi-condition filtering on numerical columns",
            "D) The operator '&&' must be used instead of 'and' without parentheses"
        ],
        "answer": "B",
        "explanation": "Python's logical 'and' expects a single scalar boolean, raising 'The truth value of a Series is ambiguous'. Element-wise boolean combination requires bitwise '&' and parentheses around each condition."
    },
    {
        "id": 189,
        "topic": "Day 11: Pandas .loc vs .iloc",
        "question": "What is the key difference between df.loc[] and df.iloc[] in Pandas?",
        "code": None,
        "options": [
            "A) .loc is integer-position based; .iloc is label based",
            "B) .loc is label-based (using row/column names); .iloc is integer-position based (0-indexed integers)",
            "C) .loc is for rows only; .iloc is for columns only",
            "D) They are completely identical"
        ],
        "answer": "B",
        "explanation": ".loc selects by index/column labels; .iloc selects strictly by integer position."
    },
    {
        "id": 190,
        "topic": "Day 11: Pandas groupby() Aggregation",
        "question": "Consider the following Pandas DataFrame aggregation:\nimport pandas as pd\ndf = pd.DataFrame({\n    'Company': ['Lego', 'Lego', 'Duplo', 'Duplo', 'Lego'],\n    'Price': [10.0, 20.0, 15.0, 25.0, 30.0],\n    'Units': [2, 1, 3, 2, 1]\n})\ngrouped = df.groupby('Company').agg({'Price': ['mean', 'max'], 'Units': 'sum'})\nprint(grouped.shape, grouped['Price']['max']['Lego'])\nWhat is the output?",
        "code": 'import pandas as pd\ndf = pd.DataFrame({\n    "Company": ["Lego", "Lego", "Duplo", "Duplo", "Lego"],\n    "Price": [10.0, 20.0, 15.0, 25.0, 30.0],\n    "Units": [2, 1, 3, 2, 1]\n})\ngrouped = df.groupby("Company").agg({"Price": ["mean", "max"], "Units": "sum"})\nprint(grouped.shape, grouped["Price"]["max"]["Lego"])',
        "options": [
            "A) (2, 3) 30.0",
            "B) (2, 2) 30.0",
            "C) (5, 3) 20.0",
            "D) (2, 3) 20.0"
        ],
        "answer": "A",
        "explanation": "Two unique companies ('Duplo', 'Lego') yield 2 rows. Three aggregated columns: Price mean, Price max, Units sum -> shape (2, 3). Max price for Lego is 30.0."
    },
    {
        "id": 191,
        "topic": "Day 10: NumPy Boolean Masking",
        "question": "What is the output of arr[arr % 2 != 0] on arr = np.array([1, 2, 3, 4, 5])?",
        "code": None,
        "options": [
            "A) [2, 4]",
            "B) [1, 3, 5]",
            "C) [True, False, True, False, True]",
            "D) 3"
        ],
        "answer": "B",
        "explanation": "arr % 2 != 0 creates a boolean mask [True, False, True, False, True]. Indexing arr with this mask extracts [1, 3, 5]."
    },
    {
        "id": 192,
        "topic": "Day 11: Pandas Handling Missing Values",
        "question": "What is the difference between df.dropna() and df.fillna(0)?",
        "code": None,
        "options": [
            "A) dropna() removes rows/columns with NaN values; fillna(0) replaces NaN values with 0.",
            "B) dropna() replaces NaN with None; fillna(0) deletes NaN rows.",
            "C) Both delete rows with NaN.",
            "D) fillna(0) is only for string columns."
        ],
        "answer": "A",
        "explanation": "dropna() drops rows (or columns) containing null values; fillna(val) substitutes missing values with val."
    },
    {
        "id": 193,
        "topic": "Day 11: Pandas Series Creation",
        "question": "What is the index of s = pd.Series([100, 200, 300]) if no index parameter was provided?",
        "code": None,
        "options": [
            "A) ['a', 'b', 'c']",
            "B) RangeIndex(start=0, stop=3, step=1) [0, 1, 2]",
            "C) [1, 2, 3]",
            "D) None"
        ],
        "answer": "B",
        "explanation": "Pandas assigns a default integer RangeIndex starting at 0: 0, 1, 2."
    },
    {
        "id": 194,
        "topic": "Day 11: Matplotlib subplots() Return Values",
        "question": "What objects are returned by fig, ax = plt.subplots() in Matplotlib?",
        "code": 'import matplotlib.pyplot as plt\nfig, ax = plt.subplots()',
        "options": [
            "A) A canvas and a brush",
            "B) A Figure object (the overall window/page) and an Axes object (the actual plotting area)",
            "C) Two numpy arrays",
            "D) A string filepath"
        ],
        "answer": "B",
        "explanation": "plt.subplots() returns a Figure object (the top-level container) and an Axes object (or array of Axes) where plotting occurs."
    },
    {
        "id": 195,
        "topic": "Day 11: Matplotlib plt.barh()",
        "question": "What kind of chart does plt.barh() produce in Matplotlib?",
        "code": None,
        "options": [
            "A) Vertical bar chart",
            "B) Horizontal bar chart",
            "C) Histogram",
            "D) Pie chart"
        ],
        "answer": "B",
        "explanation": "barh() draws horizontal bars (categories along the y-axis, values along the x-axis)."
    },
    {
        "id": 196,
        "topic": "Day 10: NumPy Broadcasting Rules",
        "question": "What is the result of adding a 1D array of shape (3,) to a 2D array of shape (2, 3)?",
        "code": 'a = np.ones((2, 3))\nb = np.array([1, 2, 3])\nres = a + b\nprint(res.shape)',
        "options": [
            "A) ValueError: shapes not aligned",
            "B) (2, 3)",
            "C) (3, 2)",
            "D) (2, 1)"
        ],
        "answer": "B",
        "explanation": "NumPy broadcasts array b across each row of a. The resulting array retains shape (2, 3)."
    },
    {
        "id": 197,
        "topic": "Day 11: Pandas value_counts()",
        "question": "What does df['Category'].value_counts() return?",
        "code": None,
        "options": [
            "A) The total number of columns in df",
            "B) A Series containing counts of unique values in 'Category', sorted in descending order",
            "C) The mean value of 'Category'",
            "D) A boolean Series"
        ],
        "answer": "B",
        "explanation": "value_counts() computes frequencies of each unique category in descending order."
    },
    {
        "id": 198,
        "topic": "Day 10: Web Scraping robots.txt",
        "question": "What is the standard purpose of the robots.txt file hosted on web servers?",
        "code": None,
        "options": [
            "A) To configure web server firewall rules",
            "B) To inform web crawlers and scraping bots which URL paths are permitted or disallowed for scraping",
            "C) To install Python scraping packages on client machines",
            "D) To store encrypted passwords"
        ],
        "answer": "B",
        "explanation": "robots.txt outlines scraping guidelines and policies for automated web crawlers."
    },
    {
        "id": 199,
        "topic": "Day 10: Requests Library Response JSON",
        "question": "What is the cleanest way to parse JSON data from a response using Python's requests library?",
        "code": 'import requests\nresp = requests.get("https://api.example.com/data")',
        "options": [
            "A) json.loads(resp.text)",
            "B) resp.json()",
            "C) Both A and B are valid, with resp.json() being the built-in convenience method",
            "D) resp.to_dict()"
        ],
        "answer": "C",
        "explanation": "resp.json() is the built-in convenience method that decodes resp.text with json.loads(). Both are valid."
    },
    {
        "id": 200,
        "topic": "Day 11: Matplotlib plt.savefig() Placement",
        "question": "Why should plt.savefig('plot.png') typically be called BEFORE plt.show()?",
        "code": None,
        "options": [
            "A) plt.show() erases the disk file",
            "B) plt.show() clears the current figure canvas when the GUI window is closed, resulting in a blank saved image if savefig is called after",
            "C) savefig raises an error if called after show()",
            "D) Matplotlib requires saving before display for licensing reasons"
        ],
        "answer": "B",
        "explanation": "plt.show() resets the current figure state upon window close. Calling savefig() after show() often saves a blank canvas."
    }
]

with open(r"d:\Engineering\CDAC_ALL_MODULES\Python\questions_medium.py", "w", encoding="utf-8") as f:
    f.write('"""Medium Question Bank (Q101 - Q200)"""\n\n')
    f.write("MEDIUM_QUESTIONS = " + json.dumps(questions, indent=4))
print(f"Successfully generated {len(questions)} medium questions.")
