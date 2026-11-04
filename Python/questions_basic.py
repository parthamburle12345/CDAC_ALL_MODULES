null = None
false = False
true = True

BASIC_QUESTIONS = [
    {
        "id": 1,
        "topic": "Day 01: Python History & Origins",
        "question": "Who created the Python programming language and in which year was it first released?",
        "code": null,
        "options": [
            "A) Guido van Rossum, 1991",
            "B) James Gosling, 1995",
            "C) Bjarne Stroustrup, 1985",
            "D) Dennis Ritchie, 1972"
        ],
        "answer": "A",
        "explanation": "Guido van Rossum developed Python in the late 1980s and first released it in February 1991."
    },
    {
        "id": 2,
        "topic": "Day 01: Language Architecture",
        "question": "How is Python source code (.py) executed by the standard CPython runtime?",
        "code": null,
        "options": [
            "A) It is purely interpreted line-by-line without any bytecode compilation stage.",
            "B) It is translated into C code and compiled using GCC.",
            "C) It is directly compiled into hardware machine code.",
            "D) It is compiled into bytecode (.pyc) and then executed by the Python Virtual Machine (PVM)."
        ],
        "answer": "D",
        "explanation": "CPython first compiles source code into intermediate bytecode (.pyc), which is then interpreted by the Python Virtual Machine (PVM)."
    },
    {
        "id": 3,
        "topic": "Day 01: Output Formatting",
        "question": "What is the output of the following print statement?",
        "code": "print(\"Python\", \"CDAC\", \"2026\", sep=\"::\")",
        "options": [
            "A) Python::CDAC::2026::",
            "B) Python CDAC 2026",
            "C) Python::CDAC::2026",
            "D) Python, CDAC, 2026"
        ],
        "answer": "C",
        "explanation": "The sep parameter specifies the separator placed between positional arguments in print()."
    },
    {
        "id": 4,
        "topic": "Day 01: Print Formatting",
        "question": "What is printed by the following code snippet?",
        "code": "print(\"Hello\", end=\"***\")\nprint(\"World\")",
        "options": [
            "A) Hello\\n***World",
            "B) Hello***World",
            "C) Hello World",
            "D) Hello***\\nWorld"
        ],
        "answer": "B",
        "explanation": "The end parameter replaces the default newline (\\n). Setting end='***' appends '***' without starting a new line."
    },
    {
        "id": 5,
        "topic": "Day 01: Input Handling",
        "question": "What is the return data type of Python's built-in input() function?",
        "code": "val = input(\"Enter a number: \")",
        "options": [
            "A) float if decimals are entered",
            "B) str always",
            "C) Based on dynamic type inference",
            "D) int if only digits are entered"
        ],
        "answer": "B",
        "explanation": "input() always reads input from standard input as a string (str), requiring explicit casting (e.g., int())."
    },
    {
        "id": 6,
        "topic": "Day 01: Identifiers & Naming Rules",
        "question": "Which of the following is a valid variable identifier in Python?",
        "code": null,
        "options": [
            "A) _student_score_2",
            "B) class",
            "C) 2nd_record",
            "D) total-amount"
        ],
        "answer": "A",
        "explanation": "Variable names cannot start with a digit, cannot contain hyphens (-), and cannot be reserved keywords ('class')."
    },
    {
        "id": 7,
        "topic": "Day 01: Floor Division",
        "question": "What is the output of the following arithmetic expressions?",
        "code": "print(10 // 3, -10 // 3)",
        "options": [
            "A) 3.0 -4.0",
            "B) 3 -3",
            "C) 3 -4",
            "D) 3.33 -3.33"
        ],
        "answer": "C",
        "explanation": "Floor division // rounds down towards negative infinity. 10 // 3 is 3, while -10 // 3 (-3.333) rounds down to -4."
    },
    {
        "id": 8,
        "topic": "Day 01: Division Operator",
        "question": "What is the data type and value of the result of 12 / 4 in Python 3?",
        "code": "res = 12 / 4\nprint(type(res), res)",
        "options": [
            "A) <class 'int'> 3",
            "B) <class 'float'> 3.0",
            "C) <class 'int'> 3.0",
            "D) <class 'float'> 3"
        ],
        "answer": "B",
        "explanation": "The single slash division operator / always returns a float in Python 3, even if the division is exact."
    },
    {
        "id": 9,
        "topic": "Day 01: Exponentiation Operator",
        "question": "What is the output of the following arithmetic expression?",
        "code": "print(2 ** 3 ** 2)",
        "options": [
            "A) 512",
            "B) 36",
            "C) 128",
            "D) 64"
        ],
        "answer": "A",
        "explanation": "The exponentiation operator ** has right-to-left associativity: 3 ** 2 = 9, then 2 ** 9 = 512."
    },
    {
        "id": 10,
        "topic": "Day 01: Modulo Operator",
        "question": "What is the output of evaluating 17 % 5 in Python?",
        "code": null,
        "options": [
            "A) 3.4",
            "B) 1",
            "C) 3",
            "D) 2"
        ],
        "answer": "D",
        "explanation": "The modulo operator % returns the remainder of division: 17 = 5 * 3 + 2, so 17 % 5 is 2."
    },
    {
        "id": 11,
        "topic": "Day 01: Identity vs Equality",
        "question": "What is the fundamental difference between the '==' operator and the 'is' operator?",
        "code": null,
        "options": [
            "A) They are completely synonymous and interchangeable.",
            "B) '==' compares memory addresses, whereas 'is' compares values.",
            "C) '==' compares values/equality, whereas 'is' compares object identity (memory addresses).",
            "D) '==' is used only for numbers, while 'is' is used only for strings."
        ],
        "answer": "C",
        "explanation": "'==' checks value equality (__eq__), while 'is' checks if both variables refer to the exact same object in memory (id(a) == id(b))."
    },
    {
        "id": 12,
        "topic": "Day 01: Membership Operators",
        "question": "What is the output of the following code snippet?",
        "code": "fruits = [\"apple\", \"banana\", \"cherry\"]\nprint(\"ban\" in fruits, \"banana\" in fruits)",
        "options": [
            "A) True True",
            "B) False True",
            "C) True False",
            "D) False False"
        ],
        "answer": "B",
        "explanation": "For a list, the 'in' operator checks for exact item equality, not substrings. 'ban' is not an element, but 'banana' is."
    },
    {
        "id": 13,
        "topic": "Day 01: Type Casting",
        "question": "Which of the following type conversions will raise a ValueError?",
        "code": null,
        "options": [
            "A) float('3.14')",
            "B) int('45.67')",
            "C) bool('False')",
            "D) int('100')"
        ],
        "answer": "B",
        "explanation": "int() cannot directly parse a string containing a decimal point ('45.67'). It must first be cast to float, or an integer string."
    },
    {
        "id": 14,
        "topic": "Day 01: Boolean Evaluation",
        "question": "What is the output of bool('False') in Python?",
        "code": "print(bool(\"False\"), bool(\"\"))",
        "options": [
            "A) False True",
            "B) True True",
            "C) False False",
            "D) True False"
        ],
        "answer": "D",
        "explanation": "Any non-empty string in Python evaluates to True in a boolean context. The empty string '' evaluates to False."
    },
    {
        "id": 15,
        "topic": "Day 01: Ternary Operator",
        "question": "What is the correct syntax for Python's conditional (ternary) expression?",
        "code": null,
        "options": [
            "A) value_if_true when condition otherwise value_if_false",
            "B) condition ? value_if_true : value_if_false",
            "C) value_if_true if condition else value_if_false",
            "D) if condition then value_if_true else value_if_false"
        ],
        "answer": "C",
        "explanation": "Python uses the inline ternary syntax: 'x if condition else y'."
    },
    {
        "id": 16,
        "topic": "Day 01: Range Function",
        "question": "What sequence of integers is generated by list(range(2, 9, 3))?",
        "code": null,
        "options": [
            "A) [2, 5, 8]",
            "B) [2, 5, 8, 11]",
            "C) [3, 6, 9]",
            "D) [2, 3, 4, 5, 6, 7, 8]"
        ],
        "answer": "A",
        "explanation": "range(start, stop, step) starts at 2, increments by 3, and stops before 9: [2, 5, 8]."
    },
    {
        "id": 17,
        "topic": "Day 01: Range Defaults",
        "question": "What is produced by list(range(5))?",
        "code": null,
        "options": [
            "A) [0, 1, 2, 3, 4]",
            "B) [0, 1, 2, 3, 4, 5]",
            "C) [5]",
            "D) [1, 2, 3, 4, 5]"
        ],
        "answer": "A",
        "explanation": "When a single argument is passed to range(stop), start defaults to 0 and step defaults to 1."
    },
    {
        "id": 18,
        "topic": "Day 01: Loop Control Statements",
        "question": "What does the break statement do when encountered inside a loop?",
        "code": null,
        "options": [
            "A) Restarts the loop from the first iteration.",
            "B) Exits the entire Python program.",
            "C) Skips the current iteration and jumps to the next iteration.",
            "D) Immediately terminates the innermost loop."
        ],
        "answer": "D",
        "explanation": "break immediately terminates the innermost enclosing loop."
    },
    {
        "id": 19,
        "topic": "Day 01: Continue Statement",
        "question": "What is the output of the following code snippet?",
        "code": "total = 0\nfor i in range(5):\n    if i % 2 == 0:\n        continue\n    total += i\nprint(total)",
        "options": [
            "A) 0",
            "B) 10",
            "C) 6",
            "D) 4"
        ],
        "answer": "D",
        "explanation": "For i in [0, 1, 2, 3, 4], even numbers (0, 2, 4) are skipped by continue. Odds added: 1 + 3 = 4."
    },
    {
        "id": 20,
        "topic": "Day 01: For-Else Construct",
        "question": "When does the else block attached to a for or while loop execute?",
        "code": null,
        "options": [
            "A) Only if the loop was terminated prematurely by a break statement.",
            "B) Only if the loop completes normally without encountering a break statement.",
            "C) At the start of every iteration.",
            "D) Only if an unhandled exception occurs inside the loop."
        ],
        "answer": "B",
        "explanation": "A loop's else clause executes if and only if the loop exits naturally without hitting a break statement."
    },
    {
        "id": 21,
        "topic": "Day 01: Pass Statement",
        "question": "What is the purpose of the pass statement in Python?",
        "code": null,
        "options": [
            "A) It acts as a null statement / placeholder where code is syntactically required but no action is needed.",
            "B) It forces the interpreter to skip garbage collection.",
            "C) It passes execution to the next function.",
            "D) To pass a variable to another scope."
        ],
        "answer": "A",
        "explanation": "pass is a null operation. It serves as a syntactic placeholder."
    },
    {
        "id": 22,
        "topic": "Day 01: Logical Operators",
        "question": "What is the output of evaluating not (5 > 3 and 2 == 1)?",
        "code": null,
        "options": [
            "A) None",
            "B) 1",
            "C) False",
            "D) True"
        ],
        "answer": "D",
        "explanation": "(5 > 3) is True, (2 == 1) is False. True and False is False. not (False) is True."
    },
    {
        "id": 23,
        "topic": "Day 01: Bitwise Operators",
        "question": "What is the result of the bitwise operation 5 & 3 in Python?",
        "code": null,
        "options": [
            "A) 2",
            "B) 7",
            "C) 1",
            "D) 8"
        ],
        "answer": "C",
        "explanation": "5 is 0b101, 3 is 0b011. Bitwise AND: 101 & 011 = 001 (which is integer 1)."
    },
    {
        "id": 24,
        "topic": "Day 01: Bitwise XOR",
        "question": "What is the output of 6 ^ 3 in Python?",
        "code": null,
        "options": [
            "A) 216",
            "B) 5",
            "C) 9",
            "D) 7"
        ],
        "answer": "B",
        "explanation": "^ is bitwise XOR (not exponentiation). 6 is 110 in binary, 3 is 011. 110 ^ 011 = 101 (which is 5)."
    },
    {
        "id": 25,
        "topic": "Day 01: Built-in type() and id()",
        "question": "Which built-in function returns the unique integer memory identity of a Python object?",
        "code": null,
        "options": [
            "A) id()",
            "B) ref()",
            "C) hash()",
            "D) type()"
        ],
        "answer": "A",
        "explanation": "id(obj) returns the identity of an object, which is guaranteed to be unique and constant for its lifetime (in CPython, its memory address)."
    },
    {
        "id": 26,
        "topic": "Day 02: String Immutability",
        "question": "What happens when you execute the following code?",
        "code": "s = \"Python\"\ns[0] = \"J\"",
        "options": [
            "A) ValueError: strings cannot be modified",
            "B) SyntaxError: invalid assignment",
            "C) s becomes 'Jython'",
            "D) TypeError: 'str' object does not support item assignment"
        ],
        "answer": "D",
        "explanation": "Python strings are strictly immutable. Modifying an individual character by index raises a TypeError."
    },
    {
        "id": 27,
        "topic": "Day 02: Basic Slicing",
        "question": "What is the output of text[1:5] where text = 'PROGRAM'?",
        "code": "text = \"PROGRAM\"\nprint(text[1:5])",
        "options": [
            "A) ROGRA",
            "B) PROG",
            "C) ROGR",
            "D) ROCR"
        ],
        "answer": "C",
        "explanation": "Indices 1 up to (but excluding) 5: text[1]='R', text[2]='O', text[3]='G', text[4]='R'. Output: 'ROGR'."
    },
    {
        "id": 28,
        "topic": "Day 02: Negative Slicing",
        "question": "What is the output of text[-3:] where text = 'DEVELOPER'?",
        "code": "text = \"DEVELOPER\"\nprint(text[-3:])",
        "options": [
            "A) PER",
            "B) OPE",
            "C) LOP",
            "D) REP"
        ],
        "answer": "A",
        "explanation": "Negative index -3 points to 'P'. text[-3:] extracts from index -3 to the end of the string: 'PER'."
    },
    {
        "id": 29,
        "topic": "Day 02: String Reversal",
        "question": "Which of the following expressions reverses a string s using slice notation?",
        "code": null,
        "options": [
            "A) s[::-1]",
            "B) s[-1:0]",
            "C) s[1:len(s):-1]",
            "D) s[0:-1]"
        ],
        "answer": "A",
        "explanation": "s[::-1] starts from the end and steps backward by -1 across the entire string, producing the reversed string."
    },
    {
        "id": 30,
        "topic": "Day 02: String Stripping",
        "question": "What does the strip() method do on a string?",
        "code": "s = \"  hello world  \\n\"\nprint(repr(s.strip()))",
        "options": [
            "A) Removes only trailing newlines.",
            "B) Converts the string to lowercase.",
            "C) Removes all spaces from everywhere inside the string.",
            "D) Removes leading and trailing whitespace characters."
        ],
        "answer": "D",
        "explanation": "strip() removes leading and trailing whitespace characters (spaces, tabs, newlines) from both ends."
    },
    {
        "id": 31,
        "topic": "Day 02: String Splitting",
        "question": "What is the output of s.split(',') when s = 'apple,banana,orange'?",
        "code": "s = \"apple,banana,orange\"\nprint(s.split(\",\"))",
        "options": [
            "A) 'apple banana orange'",
            "B) ('apple', 'banana', 'orange')",
            "C) ['apple', 'banana', 'orange']",
            "D) {'apple', 'banana', 'orange'}"
        ],
        "answer": "C",
        "explanation": "split() splits a string by a given delimiter and returns a list of strings."
    },
    {
        "id": 32,
        "topic": "Day 02: String Joining",
        "question": "What is the output of the following code snippet?",
        "code": "words = [\"AI\", \"ML\", \"DL\"]\nprint(\"-\".join(words))",
        "options": [
            "A) AI ML DL",
            "B) AI-ML-DL",
            "C) -AI-ML-DL-",
            "D) ['AI', 'ML', 'DL']"
        ],
        "answer": "B",
        "explanation": "'-'.join(iterable) joins the elements of an iterable using '-' as the separator."
    },
    {
        "id": 33,
        "topic": "Day 02: find() vs index()",
        "question": "What happens when you search for a substring that is NOT found using find() vs index()?",
        "code": null,
        "options": [
            "A) Both raise a ValueError.",
            "B) find() returns -1, while index() raises a ValueError.",
            "C) find() raises ValueError, while index() returns None.",
            "D) Both return -1."
        ],
        "answer": "B",
        "explanation": "str.find() safely returns -1 when a substring is not found, whereas str.index() raises a ValueError."
    },
    {
        "id": 34,
        "topic": "Day 02: String Case Methods",
        "question": "What is the output of 'python programming'.title()?",
        "code": null,
        "options": [
            "A) 'PYTHON PROGRAMMING'",
            "B) 'Python Programming.'",
            "C) 'Python programming'",
            "D) 'Python Programming'"
        ],
        "answer": "D",
        "explanation": "title() capitalizes the first character of each word in the string."
    },
    {
        "id": 35,
        "topic": "Day 02: Raw Strings",
        "question": "What is the output of printing a raw string r'C:\\new\\test'?",
        "code": "path = r\"C:\\new\\test\"\nprint(path)",
        "options": [
            "A) SyntaxError",
            "B) C: followed by a newline then ew\\test",
            "C) C:\\new\\test",
            "D) C:\\new followed by a tab"
        ],
        "answer": "C",
        "explanation": "Prefixing a string with 'r' creates a raw string literal, where backslashes are treated as literal characters, not escape sequences."
    },
    {
        "id": 36,
        "topic": "Day 02: String Formatting (f-strings)",
        "question": "What is the output of the following f-string with a float precision specifier?",
        "code": "pi = 3.1415926\nprint(f\"Pi is {pi:.2f}\")",
        "options": [
            "A) Pi is 3.1415926",
            "B) Pi is 3.14",
            "C) Pi is 3.15",
            "D) Pi is 3.1"
        ],
        "answer": "B",
        "explanation": "{pi:.2f} formats the floating point number to 2 decimal places with standard rounding (3.14)."
    },
    {
        "id": 37,
        "topic": "Day 02: String replace()",
        "question": "What is the output of the following code snippet?",
        "code": "msg = \"java is cool\"\nmsg.replace(\"java\", \"python\")\nprint(msg)",
        "options": [
            "A) java is cool",
            "B) None",
            "C) TypeError",
            "D) python is cool"
        ],
        "answer": "A",
        "explanation": "Strings are immutable! replace() returns a new string; it does NOT modify msg in place. Since the return value wasn't reassigned, msg remains 'java is cool'."
    },
    {
        "id": 38,
        "topic": "Day 02: String startswith()",
        "question": "What is the return value of 'https://cdac.in'.startswith(('http://', 'https://'))?",
        "code": null,
        "options": [
            "A) TypeError: startswith does not take a tuple",
            "B) None",
            "C) True",
            "D) False"
        ],
        "answer": "C",
        "explanation": "str.startswith() accepts a tuple of prefixes and returns True if the string starts with any of them."
    },
    {
        "id": 39,
        "topic": "Day 02: String Character Check",
        "question": "What is the output of '1234a'.isdigit() and '1234'.isdigit()?",
        "code": null,
        "options": [
            "A) False False",
            "B) True True",
            "C) False True",
            "D) True False"
        ],
        "answer": "C",
        "explanation": "isdigit() returns True only if all characters in the string are digits. '1234a' contains 'a', so it returns False."
    },
    {
        "id": 40,
        "topic": "Day 02: String Repetition",
        "question": "What is the output of '=' * 5?",
        "code": null,
        "options": [
            "A) TypeError: cannot multiply string by int",
            "B) '====='",
            "C) '5'",
            "D) '== = = ='"
        ],
        "answer": "B",
        "explanation": "The multiplication operator * on a string repeats it the specified number of times: '====='."
    },
    {
        "id": 41,
        "topic": "Day 02: String count()",
        "question": "What is the output of 'banana'.count('an')?",
        "code": null,
        "options": [
            "A) 2",
            "B) 3",
            "C) 0",
            "D) 1"
        ],
        "answer": "A",
        "explanation": "'banana' contains non-overlapping occurrences of 'an' at indices 1 and 3, so count('an') returns 2."
    },
    {
        "id": 42,
        "topic": "Day 02: String Multiline",
        "question": "How are multiline string literals defined in Python?",
        "code": null,
        "options": [
            "A) Using the multiline keyword",
            "B) Ending every line with a comma",
            "C) Enclosing in single backticks `...`",
            "D) Enclosing in triple single ('''...''') or triple double (\"\"\"...\"\"\") quotes"
        ],
        "answer": "D",
        "explanation": "Triple quotes (''' or \"\"\") allow string literals to span multiple lines, preserving line breaks and indents."
    },
    {
        "id": 43,
        "topic": "Day 02: String Concatenation",
        "question": "What is the output of 'Hello ' + 'World' vs 'Hello ' * 2?",
        "code": null,
        "options": [
            "A) 'HelloWorld' and 'HelloHello'",
            "B) 'HelloWorld' and 'Hello Hello '",
            "C) 'Hello World' and 'Hello Hello '",
            "D) 'Hello World' and 'HelloHello'"
        ],
        "answer": "C",
        "explanation": "'Hello ' + 'World' concatenates to 'Hello World', while 'Hello ' * 2 repeats the string to 'Hello Hello '."
    },
    {
        "id": 44,
        "topic": "Day 02: len() Function",
        "question": "What is the output of len('Hello\\nWorld')?",
        "code": null,
        "options": [
            "A) 12",
            "B) 11",
            "C) 10",
            "D) 13"
        ],
        "answer": "B",
        "explanation": "'Hello' is 5 chars, '\\n' is a single escape character (1 char), and 'World' is 5 chars. Total length = 5 + 1 + 5 = 11."
    },
    {
        "id": 45,
        "topic": "Day 02: String Formatting (% vs format)",
        "question": "What is the output of 'Item: %s, Price: %.1f' % ('Book', 19.95)?",
        "code": null,
        "options": [
            "A) Item: Book, Price: 20.0",
            "B) Item: Book, Price: 19.9",
            "C) Item: Book, Price: 20",
            "D) Item: Book, Price: 19.95"
        ],
        "answer": "A",
        "explanation": "%.1f rounds 19.95 to 1 decimal place, producing 20.0."
    },
    {
        "id": 46,
        "topic": "Day 03: List Mutability",
        "question": "Which of the following operations on a Python list is valid?",
        "code": "nums = [10, 20, 30]\nnums[1] = 99",
        "options": [
            "A) Raises IndexError",
            "B) Appends 99 to the end of the list",
            "C) Raises TypeError because lists are immutable",
            "D) Modifies the list to [10, 99, 30]"
        ],
        "answer": "D",
        "explanation": "Lists are mutable sequences. Item assignment by index modifies the element in place."
    },
    {
        "id": 47,
        "topic": "Day 03: Single Element Tuple",
        "question": "Which of the following correctly defines a single-element tuple containing the integer 42?",
        "code": null,
        "options": [
            "A) t = {42}",
            "B) t = (42)",
            "C) t = [42]",
            "D) t = (42,)"
        ],
        "answer": "D",
        "explanation": "In Python, parentheses alone do not create a tuple; a trailing comma is required: (42,). (42) is simply the integer 42."
    },
    {
        "id": 48,
        "topic": "Day 03: list.append() vs list.extend()",
        "question": "What is the output of the following code snippet?",
        "code": "a = [1, 2]\na.append([3, 4])\nb = [1, 2]\nb.extend([3, 4])\nprint(len(a), len(b))",
        "options": [
            "A) 4 4",
            "B) 3 4",
            "C) 3 3",
            "D) 4 3"
        ],
        "answer": "B",
        "explanation": "append() adds the argument as a single element ([1, 2, [3, 4]], len=3). extend() unpacks and iterates over the elements ([1, 2, 3, 4], len=4)."
    },
    {
        "id": 49,
        "topic": "Day 03: list.insert()",
        "question": "What is the output of list.insert(1, 'X') on nums = ['A', 'B', 'C']?",
        "code": "nums = ['A', 'B', 'C']\nnums.insert(1, 'X')\nprint(nums)",
        "options": [
            "A) ['A', 'X', 'B', 'C']",
            "B) ['A', 'B', 'X', 'C']",
            "C) ['A', 'X', 'C']",
            "D) ['X', 'A', 'B', 'C']"
        ],
        "answer": "A",
        "explanation": "insert(index, element) inserts the element before the given index, shifting subsequent elements to the right."
    },
    {
        "id": 50,
        "topic": "Day 03: list.pop()",
        "question": "What does list.pop() without arguments do, and what does it return?",
        "code": "nums = [10, 20, 30]\nval = nums.pop()\nprint(val, nums)",
        "options": [
            "A) Returns None and empties the list",
            "B) Raises an error because index argument is required",
            "C) Removes and returns the first element (10)",
            "D) Removes and returns the last element (30)"
        ],
        "answer": "D",
        "explanation": "pop() without arguments removes and returns the last item in the list."
    },
    {
        "id": 51,
        "topic": "Day 03: list.remove()",
        "question": "What happens when you call nums.remove(99) if 99 is not in nums = [1, 2, 3]?",
        "code": null,
        "options": [
            "A) It does nothing silently",
            "B) It returns -1",
            "C) It returns False",
            "D) It raises a ValueError"
        ],
        "answer": "D",
        "explanation": "list.remove(x) searches for the first occurrence of x and deletes it. If x is not found, it raises a ValueError."
    },
    {
        "id": 52,
        "topic": "Day 03: Tuple Immutability",
        "question": "What is the output of attempting to modify a tuple?",
        "code": "t = (1, 2, 3)\nt[0] = 10",
        "options": [
            "A) t becomes (10, 2, 3)",
            "B) TypeError: 'tuple' object does not support item assignment",
            "C) ValueError: tuples cannot be changed",
            "D) AttributeError: tuple has no set attribute"
        ],
        "answer": "B",
        "explanation": "Tuples are immutable sequences. Modifying elements by index raises a TypeError."
    },
    {
        "id": 53,
        "topic": "Day 03: Tuple Unpacking",
        "question": "What is the output of the following tuple unpacking statement?",
        "code": "a, b, c = (10, 20, 30)\nprint(b)",
        "options": [
            "A) 20",
            "B) 30",
            "C) (10, 20)",
            "D) 10"
        ],
        "answer": "A",
        "explanation": "The elements of the tuple (10, 20, 30) are unpacked into variables a, b, c. Therefore, b = 20."
    },
    {
        "id": 54,
        "topic": "Day 03: Variable Swap",
        "question": "How does Python swap two variables x and y in a single line without a temporary variable?",
        "code": null,
        "options": [
            "A) x, y = y, x",
            "B) x = y; y = x",
            "C) x.swap(y)",
            "D) swap(x, y)"
        ],
        "answer": "A",
        "explanation": "Python evaluates the right side into a tuple (y, x) first and then unpacks it into the left side: x, y = y, x."
    },
    {
        "id": 55,
        "topic": "Day 03: List Comprehension Basics",
        "question": "What does the list comprehension [x * 2 for x in range(4)] produce?",
        "code": null,
        "options": [
            "A) [0, 2, 4, 6, 8]",
            "B) [0, 2, 4, 6]",
            "C) [2, 4, 6, 8]",
            "D) [0, 1, 2, 3]"
        ],
        "answer": "B",
        "explanation": "range(4) produces 0, 1, 2, 3. Multiplying each by 2 yields [0, 2, 4, 6]."
    },
    {
        "id": 56,
        "topic": "Day 03: List Comprehension with Filter",
        "question": "What is the output of [x for x in range(10) if x % 3 == 0]?",
        "code": null,
        "options": [
            "A) [3, 6, 9]",
            "B) [0, 3, 6, 9]",
            "C) [0, 3, 6, 9, 12]",
            "D) [1, 3, 6, 9]"
        ],
        "answer": "B",
        "explanation": "range(10) is 0 through 9. Numbers divisible by 3 (x % 3 == 0) are 0, 3, 6, and 9."
    },
    {
        "id": 57,
        "topic": "Day 03: list.sort() vs sorted()",
        "question": "What is the difference between nums.sort() and sorted(nums)?",
        "code": null,
        "options": [
            "A) nums.sort() sorts in place and returns None; sorted(nums) returns a new sorted list.",
            "B) sorted(nums) modifies in place; nums.sort() returns a new list.",
            "C) sorted() works only on numbers; sort() works on all types.",
            "D) Both sort the list in place and return None."
        ],
        "answer": "A",
        "explanation": "list.sort() is a method that sorts the list in place and returns None. sorted(iterable) is a built-in function that leaves the original iterable unchanged and returns a new list."
    },
    {
        "id": 58,
        "topic": "Day 03: list.index()",
        "question": "What is the output of [10, 20, 30, 20].index(20)?",
        "code": null,
        "options": [
            "A) [1, 3]",
            "B) 2",
            "C) 1",
            "D) 3"
        ],
        "answer": "C",
        "explanation": "index() returns the zero-based index of the FIRST occurrence of the specified value. The first 20 is at index 1."
    },
    {
        "id": 59,
        "topic": "Day 03: del Statement",
        "question": "What is the output of the following code snippet?",
        "code": "nums = [1, 2, 3, 4]\ndel nums[1:3]\nprint(nums)",
        "options": [
            "A) []",
            "B) [1, 4]",
            "C) [1, 2, 4]",
            "D) [2, 3]"
        ],
        "answer": "B",
        "explanation": "del nums[1:3] deletes elements from index 1 up to (excluding) 3, which are 2 and 3. Remaining elements: [1, 4]."
    },
    {
        "id": 60,
        "topic": "Day 03: Built-in min, max, sum",
        "question": "What is the output of print(min(nums), max(nums), sum(nums)) where nums = [4, 1, 7, 2]?",
        "code": null,
        "options": [
            "A) 1 7 14",
            "B) 1 7 12",
            "C) 4 7 14",
            "D) 1 4 14"
        ],
        "answer": "A",
        "explanation": "min is 1, max is 7, and sum is 4 + 1 + 7 + 2 = 14."
    },
    {
        "id": 61,
        "topic": "Day 04: Dictionary Key Requirements",
        "question": "Which of the following data types CANNOT be used as a key in a Python dictionary?",
        "code": null,
        "options": [
            "A) int",
            "B) tuple of strings",
            "C) list",
            "D) str"
        ],
        "answer": "C",
        "explanation": "Dictionary keys must be hashable (immutable). Lists are mutable and unhashable, so they cannot serve as dictionary keys."
    },
    {
        "id": 62,
        "topic": "Day 04: Dictionary Access (.get)",
        "question": "What happens when you access a non-existent key using d['unknown'] vs d.get('unknown', 0)?",
        "code": null,
        "options": [
            "A) d['unknown'] raises KeyError, while d.get('unknown', 0) returns 0.",
            "B) d['unknown'] returns None, while d.get() raises KeyError.",
            "C) Both raise KeyError.",
            "D) Both return 0."
        ],
        "answer": "A",
        "explanation": "Direct indexing d[key] raises KeyError if key is missing. d.get(key, default) safely returns default (or None)."
    },
    {
        "id": 63,
        "topic": "Day 04: dict.keys() & dict.values()",
        "question": "What is the output of the following dictionary operations?",
        "code": "d = {\"a\": 1, \"b\": 2}\nprint(list(d.keys()), list(d.values()))",
        "options": [
            "A) {'a', 'b'} {1, 2}",
            "B) ['a', 'b'] [1, 2]",
            "C) [1, 2] ['a', 'b']",
            "D) [('a', 1), ('b', 2)]"
        ],
        "answer": "B",
        "explanation": "d.keys() provides a view of keys ('a', 'b') and d.values() provides a view of values (1, 2)."
    },
    {
        "id": 64,
        "topic": "Day 04: dict.pop()",
        "question": "What is the output of data.pop('c', 99) where data = {'a': 10, 'b': 20}?",
        "code": "data = {\"a\": 10, \"b\": 20}\nres = data.pop(\"c\", 99)\nprint(res)",
        "options": [
            "A) KeyError",
            "B) None",
            "C) 99",
            "D) {'a': 10, 'b': 20}"
        ],
        "answer": "C",
        "explanation": "dict.pop(key, default) removes and returns the value for key; if key is not found and default is provided, it returns default."
    },
    {
        "id": 65,
        "topic": "Day 04: dict.update()",
        "question": "What does d1.update(d2) do?",
        "code": "d1 = {\"a\": 1, \"b\": 2}\nd2 = {\"b\": 99, \"c\": 3}\nd1.update(d2)\nprint(d1)",
        "options": [
            "A) {'a': 1, 'b': 99, 'c': 3}",
            "B) {'b': 99, 'c': 3}",
            "C) Raises KeyError on duplicate key 'b'",
            "D) {'a': 1, 'b': 2, 'c': 3}"
        ],
        "answer": "A",
        "explanation": "update() overwrites matching keys from d2 into d1 and adds any new keys from d2."
    },
    {
        "id": 66,
        "topic": "Day 04: Empty Set vs Empty Dict",
        "question": "What are the data types of obj1 = {} and obj2 = set()?",
        "code": "obj1 = {}\nobj2 = set()",
        "options": [
            "A) obj1 is dict, obj2 is set",
            "B) Both are dicts",
            "C) Both are sets",
            "D) obj1 is set, obj2 is dict"
        ],
        "answer": "A",
        "explanation": "Empty curly braces {} create an empty dictionary (dict). An empty set must be created using the constructor set()."
    },
    {
        "id": 67,
        "topic": "Day 04: Set Uniqueness",
        "question": "What is the output of len(set([1, 2, 2, 3, 3, 3, 4]))?",
        "code": null,
        "options": [
            "A) 1",
            "B) 7",
            "C) 4",
            "D) 3"
        ],
        "answer": "C",
        "explanation": "Sets only store unique elements. Duplicates are discarded, leaving {1, 2, 3, 4}, so len is 4."
    },
    {
        "id": 68,
        "topic": "Day 04: Set Operations (Union)",
        "question": "What is the result of {1, 2, 3} | {3, 4, 5} in Python?",
        "code": null,
        "options": [
            "A) {3}",
            "B) {1, 2, 3, 4, 5}",
            "C) {1, 2, 4, 5}",
            "D) [1, 2, 3, 4, 5]"
        ],
        "answer": "B",
        "explanation": "The pipe operator | computes the union of two sets, returning all unique elements across both sets: {1, 2, 3, 4, 5}."
    },
    {
        "id": 69,
        "topic": "Day 04: Set Operations (Intersection)",
        "question": "What is the result of {1, 2, 3} & {2, 3, 4}?",
        "code": null,
        "options": [
            "A) {2, 3}",
            "B) {1, 2, 3, 4}",
            "C) set()",
            "D) {1, 4}"
        ],
        "answer": "A",
        "explanation": "The ampersand operator & computes the intersection, returning elements present in both sets: {2, 3}."
    },
    {
        "id": 70,
        "topic": "Day 04: Set Operations (Difference)",
        "question": "What is the result of {1, 2, 3, 4} - {2, 4, 6}?",
        "code": null,
        "options": [
            "A) {1, 3, 6}",
            "B) {2, 4}",
            "C) {1, 3}",
            "D) {6}"
        ],
        "answer": "C",
        "explanation": "The minus operator - computes the set difference: elements in the first set but NOT in the second set: {1, 3}."
    },
    {
        "id": 71,
        "topic": "Day 04: set.discard() vs set.remove()",
        "question": "What happens when you call s.discard(99) vs s.remove(99) on s = {1, 2, 3}?",
        "code": null,
        "options": [
            "A) Both return False.",
            "B) Both raise KeyError.",
            "C) remove() raises KeyError, while discard() does nothing and raises no error.",
            "D) discard() raises KeyError, while remove() does nothing."
        ],
        "answer": "C",
        "explanation": "s.remove(x) raises a KeyError if x is not in s. s.discard(x) removes x if present, and does nothing if absent."
    },
    {
        "id": 72,
        "topic": "Day 04: Dictionary Comprehension",
        "question": "What does the dictionary comprehension {x: x**2 for x in range(3)} produce?",
        "code": null,
        "options": [
            "A) {0: 0, 1: 1, 2: 4}",
            "B) {1: 1, 2: 4, 3: 9}",
            "C) [0, 1, 4]",
            "D) {(0, 0), (1, 1), (2, 4)}"
        ],
        "answer": "A",
        "explanation": "range(3) is 0, 1, 2. Each key x is mapped to x**2: {0: 0, 1: 1, 2: 4}."
    },
    {
        "id": 73,
        "topic": "Day 04: Iterating Dictionary",
        "question": "When iterating over a dictionary using 'for item in d:', what does 'item' represent?",
        "code": "d = {\"x\": 10, \"y\": 20}\nfor item in d:\n    print(item)",
        "options": [
            "A) The keys: 'x', 'y'",
            "B) Tuples of (key, value): ('x', 10), ('y', 20)",
            "C) A single list of all items",
            "D) The values: 10, 20"
        ],
        "answer": "A",
        "explanation": "Iterating directly over a dictionary defaults to iterating over its keys."
    },
    {
        "id": 74,
        "topic": "Day 04: dict.items()",
        "question": "What does dict.items() yield during iteration?",
        "code": null,
        "options": [
            "A) (key, value) 2-element tuples",
            "B) Sub-dictionaries",
            "C) Only the keys",
            "D) Only the values"
        ],
        "answer": "A",
        "explanation": "d.items() provides key-value pairs as (key, value) tuples."
    },
    {
        "id": 75,
        "topic": "Day 04: Frozenset",
        "question": "What is a frozenset in Python?",
        "code": null,
        "options": [
            "A) A set that cannot be iterated over",
            "B) A set stored on disk in frozen binary format",
            "C) An immutable, hashable version of a set that can be used as a dictionary key",
            "D) A set that only accepts frozen floating point numbers"
        ],
        "answer": "C",
        "explanation": "frozenset is an immutable set. Because it is immutable, it is hashable and can be used as a dictionary key or an element of another set."
    },
    {
        "id": 76,
        "topic": "Day 05: Function Default Return",
        "question": "What is the return value of a Python function that executes without reaching an explicit return statement?",
        "code": "def greet():\n    print(\"Hello\")\nres = greet()\nprint(res)",
        "options": [
            "A) 0",
            "B) False",
            "C) None",
            "D) '' (empty string)"
        ],
        "answer": "C",
        "explanation": "In Python, any function that does not explicitly return a value returns None by default."
    },
    {
        "id": 77,
        "topic": "Day 05: *args and **kwargs",
        "question": "In a function definition 'def func(*args, **kwargs):', what are the types of args and kwargs?",
        "code": null,
        "options": [
            "A) args is a tuple, kwargs is a dict",
            "B) args is a dict, kwargs is a list",
            "C) Both are lists",
            "D) args is a list, kwargs is a tuple"
        ],
        "answer": "A",
        "explanation": "*args collects extra positional arguments into a tuple, while **kwargs collects extra keyword arguments into a dict."
    },
    {
        "id": 78,
        "topic": "Day 05: Default Parameters",
        "question": "Which of the following function definitions is syntactically INVALID in Python?",
        "code": null,
        "options": [
            "A) def calc(a=10, b): pass",
            "B) def calc(a, b, c=20): pass",
            "C) def calc(a, b=10): pass",
            "D) def calc(a=5, b=10): pass"
        ],
        "answer": "A",
        "explanation": "SyntaxError: non-default parameter follows default parameter. Parameters with default values must appear AFTER all parameters without defaults."
    },
    {
        "id": 79,
        "topic": "Day 05: Lambda Syntax",
        "question": "Which of the following correctly defines an anonymous lambda function that squares a number?",
        "code": null,
        "options": [
            "A) square = lambda(x) { return x ** 2; }",
            "B) square = lambda x -> x ** 2",
            "C) square = lambda x: x ** 2",
            "D) square = def(x): return x ** 2"
        ],
        "answer": "C",
        "explanation": "Lambda functions use the syntax: lambda arguments: expression."
    },
    {
        "id": 80,
        "topic": "Day 05: Built-in map()",
        "question": "What is the output of list(map(lambda x: x + 1, [1, 2, 3]))?",
        "code": null,
        "options": [
            "A) [1, 2, 3]",
            "B) [2, 3, 4]",
            "C) [1, 4, 9]",
            "D) [2, 4, 6]"
        ],
        "answer": "B",
        "explanation": "map() applies the function (adding 1) to each item in the iterable, resulting in [2, 3, 4]."
    },
    {
        "id": 81,
        "topic": "Day 05: Built-in filter()",
        "question": "What does list(filter(lambda x: x > 0, [-2, 0, 3, -1, 5])) return?",
        "code": null,
        "options": [
            "A) [3, 5]",
            "B) [0, 3, 5]",
            "C) [True, False, True, False, True]",
            "D) [-2, -1]"
        ],
        "answer": "A",
        "explanation": "filter() retains only those elements for which the predicate returns True (x > 0), giving [3, 5]."
    },
    {
        "id": 82,
        "topic": "Day 05: Built-in zip()",
        "question": "What is the output of list(zip(['a', 'b'], [1, 2]))?",
        "code": null,
        "options": [
            "A) ['a', 1, 'b', 2]",
            "B) [['a', 1], ['b', 2]]",
            "C) [{'a': 1}, {'b': 2}]",
            "D) [('a', 1), ('b', 2)]"
        ],
        "answer": "D",
        "explanation": "zip() aggregates corresponding elements from each iterable into pairs of tuples: [('a', 1), ('b', 2)]."
    },
    {
        "id": 83,
        "topic": "Day 05: Built-in enumerate()",
        "question": "What does list(enumerate(['apple', 'banana'])) return?",
        "code": null,
        "options": [
            "A) [0, 1]",
            "B) [(0, 'apple'), (1, 'banana')]",
            "C) [(1, 'apple'), (2, 'banana')]",
            "D) {'apple': 0, 'banana': 1}"
        ],
        "answer": "B",
        "explanation": "enumerate() produces 2-tuples containing a 0-based counter index and the corresponding value: [(0, 'apple'), (1, 'banana')]."
    },
    {
        "id": 84,
        "topic": "Day 05: global Keyword",
        "question": "Why is the global keyword used inside a Python function?",
        "code": "x = 10\ndef modify():\n    global x\n    x = 20",
        "options": [
            "A) To make the function accessible in other files",
            "B) To allow binding/modifying a module-level variable from inside local function scope",
            "C) To prevent other threads from modifying x",
            "D) To optimize performance"
        ],
        "answer": "B",
        "explanation": "Without the global declaration, assigning to x inside a function creates a new local variable. global tells Python to modify the module-level variable."
    },
    {
        "id": 85,
        "topic": "Day 05: Regular Expressions (re.search vs re.match)",
        "question": "What is the key difference between re.match() and re.search() in Python's re module?",
        "code": null,
        "options": [
            "A) re.search() matches only at the beginning; re.match() scans anywhere.",
            "B) re.match() returns all matches; re.search() returns only the first match.",
            "C) They are identical.",
            "D) re.match() matches only at the beginning of the string; re.search() scans the entire string."
        ],
        "answer": "D",
        "explanation": "re.match() checks for a match only at the start of the string, while re.search() scans through the entire string for a match."
    },
    {
        "id": 86,
        "topic": "Day 05: RegEx Metacharacters",
        "question": "In regular expressions, which metacharacter matches any single digit character (equivalent to [0-9])?",
        "code": null,
        "options": [
            "A) \\s",
            "B) \\b",
            "C) \\w",
            "D) \\d"
        ],
        "answer": "D",
        "explanation": "\\d matches any Unicode decimal digit (equivalent to [0-9] in ASCII)."
    },
    {
        "id": 87,
        "topic": "Day 05: RegEx findall()",
        "question": "What is the return type of re.findall(r'\\d+', 'Apples: 10, Oranges: 25')?",
        "code": null,
        "options": [
            "A) An iterator",
            "B) A match object",
            "C) A list of strings: ['10', '25']",
            "D) A tuple of integers: (10, 25)"
        ],
        "answer": "C",
        "explanation": "re.findall() returns all non-overlapping matches of pattern in string as a list of strings: ['10', '25']."
    },
    {
        "id": 88,
        "topic": "Day 05: Built-in all() and any()",
        "question": "What is the output of print(any([False, 0, '']), all([True, 1, 'Python']))?",
        "code": null,
        "options": [
            "A) False True",
            "B) True True",
            "C) False False",
            "D) True False"
        ],
        "answer": "A",
        "explanation": "any() returns True if ANY element is truthy (all are falsy here, so False). all() returns True if ALL elements are truthy (all are truthy here, so True)."
    },
    {
        "id": 89,
        "topic": "Day 06: OOP self Parameter",
        "question": "In a Python class method, what does the 'self' parameter represent?",
        "code": null,
        "options": [
            "A) An explicit reference to the current instance of the class",
            "B) A global pointer to the parent class",
            "C) The memory address of the module",
            "D) A keyword referring to the class definition"
        ],
        "answer": "A",
        "explanation": "By convention, self represents the instance of the class on which the method is called, allowing access to instance attributes."
    },
    {
        "id": 90,
        "topic": "Day 06: OOP Initializer __init__",
        "question": "What is the role of the special __init__ method in a Python class?",
        "code": null,
        "options": [
            "A) It acts as the initializer/constructor to set up attributes on a newly created instance",
            "B) To convert a class into a string",
            "C) To destroy an object and free its memory",
            "D) To allocate raw memory for a new object"
        ],
        "answer": "A",
        "explanation": "__init__ is the initializer method called immediately after memory is allocated (__new__) to initialize instance attributes."
    },
    {
        "id": 91,
        "topic": "Day 06: Instance vs Class Variables",
        "question": "What is the output of the following code snippet?",
        "code": "class Student:\n    school = \"CDAC\"\n    def __init__(self, name):\n        self.name = name\ns1 = Student(\"Alice\")\ns2 = Student(\"Bob\")\nprint(s1.school, s2.school)",
        "options": [
            "A) AttributeError",
            "B) Alice Bob",
            "C) CDAC CDAC",
            "D) None None"
        ],
        "answer": "C",
        "explanation": "school is a class variable defined outside __init__. It is shared across all instances of Student."
    },
    {
        "id": 92,
        "topic": "Day 06: Basic Inheritance",
        "question": "How does class Dog inherit from class Animal in Python?",
        "code": null,
        "options": [
            "A) class Dog extends Animal:",
            "B) class Dog(Animal):",
            "C) class Dog inherits Animal:",
            "D) class Dog : public Animal:"
        ],
        "answer": "B",
        "explanation": "Python specifies base classes inside parentheses after the class name: class Dog(Animal):."
    },
    {
        "id": 93,
        "topic": "Day 06: Built-in isinstance()",
        "question": "What is the output of isinstance(5, (str, int, float))?",
        "code": null,
        "options": [
            "A) False",
            "B) TypeError",
            "C) <class 'int'>",
            "D) True"
        ],
        "answer": "D",
        "explanation": "isinstance(obj, class_or_tuple) returns True if obj is an instance of any class in the tuple. Since 5 is an int, it returns True."
    },
    {
        "id": 94,
        "topic": "Day 06: String Representation __str__",
        "question": "Which dunder method is invoked when you pass an object to print() or str()?",
        "code": null,
        "options": [
            "A) __print__",
            "B) __display__",
            "C) __repr__",
            "D) __str__"
        ],
        "answer": "D",
        "explanation": "print(obj) and str(obj) call obj.__str__() to obtain a human-readable string representation of the object."
    },
    {
        "id": 95,
        "topic": "Day 07: File open() Default Mode",
        "question": "What is the default access mode when opening a file using Python's open('data.txt')?",
        "code": null,
        "options": [
            "A) 'rb' (read binary)",
            "B) 'w' (write)",
            "C) 'r' (read text)",
            "D) 'a' (append)"
        ],
        "answer": "C",
        "explanation": "The default mode for open() is 'r' (read text mode)."
    },
    {
        "id": 96,
        "topic": "Day 07: Context Manager 'with'",
        "question": "What is the primary advantage of using the 'with' statement when opening files in Python?",
        "code": null,
        "options": [
            "A) It makes file reads run 10x faster.",
            "B) It automatically closes the file stream when the block exits, even if exceptions occur.",
            "C) It encrypts the contents on disk.",
            "D) It allows writing to read-only files."
        ],
        "answer": "B",
        "explanation": "The 'with' statement acts as a context manager (__enter__ and __exit__), guaranteeing that file descriptors are safely closed upon block exit."
    },
    {
        "id": 97,
        "topic": "Day 07: JSON Serialization",
        "question": "Which json module function converts a Python dictionary directly into a JSON formatted string?",
        "code": null,
        "options": [
            "A) json.dumps()",
            "B) json.load()",
            "C) json.loads()",
            "D) json.dump()"
        ],
        "answer": "A",
        "explanation": "json.dumps() (dump string) serializes a Python object to a JSON string. json.dump() writes directly to a file stream."
    },
    {
        "id": 98,
        "topic": "Day 09: Flask Application Setup",
        "question": "Which decorator in Flask binds a view function to an incoming HTTP URL endpoint?",
        "code": null,
        "options": [
            "A) @app.bind()",
            "B) @app.endpoint()",
            "C) @app.url()",
            "D) @app.route()"
        ],
        "answer": "D",
        "explanation": "In Flask, @app.route('/path') is the standard decorator used to map a URL pattern to a view handler function."
    },
    {
        "id": 99,
        "topic": "Day 10: HTTP Status Codes",
        "question": "Which HTTP status code signifies that a request succeeded and resulted in the creation of a new resource?",
        "code": null,
        "options": [
            "A) 301 Moved Permanently",
            "B) 200 OK",
            "C) 201 Created",
            "D) 204 No Content"
        ],
        "answer": "C",
        "explanation": "HTTP 201 Created indicates that the request was successful and led to the creation of a new resource on the server."
    },
    {
        "id": 100,
        "topic": "Day 11: Pandas DataFrame Inspection",
        "question": "Which Pandas DataFrame method displays the first 5 rows by default?",
        "code": null,
        "options": [
            "A) df.tail()",
            "B) df.first()",
            "C) df.head()",
            "D) df.preview()"
        ],
        "answer": "C",
        "explanation": "df.head() returns the first n rows (default n=5) of the DataFrame."
    }
]