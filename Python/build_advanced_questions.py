# build_advanced_questions.py
import json

questions = [
    # Day 01 - 02: Advanced Core Internals, Types, Strings (Q201 - Q215)
    {
        "id": 201,
        "topic": "Day 01: In-Place Modification inside Tuple",
        "question": "Consider the following code executing in-place addition on a list inside a tuple:\nt = (1, [2, 3])\ntry:\n    t[1] += [4]\nexcept TypeError:\n    print('Error caught')\nprint(t)\nWhat is the output?",
        "code": 't = (1, [2, 3])\ntry:\n    t[1] += [4]\nexcept TypeError:\n    print("Error caught")\nprint(t)',
        "options": [
            "A) Error caught\\n(1, [2, 3])",
            "B) Error caught\\n(1, [2, 3, 4])",
            "C) (1, [2, 3, 4])",
            "D) TypeError: cannot catch this error"
        ],
        "answer": "B",
        "explanation": "In Python, 't[1] += [4]' executes list.extend([4]) in-place (which succeeds, modifying the list to [2, 3, 4]), and then attempts to assign the result back to t[1] (which raises TypeError because tuples are immutable). Thus, the error is caught, and t shows (1, [2, 3, 4])."
    },
    {
        "id": 202,
        "topic": "Day 01: Walrus Operator (:=)",
        "question": "What is the output of the following code utilizing the walrus operator (assignment expression)?",
        "code": 'data = [1, 2, 3, 4, 5, 6]\nres = [y for x in data if (y := x * 2) > 6]\nprint(res)',
        "options": [
            "A) [8, 10, 12]",
            "B) [4, 5, 6]",
            "C) [7, 8, 9, 10, 11, 12]",
            "D) SyntaxError"
        ],
        "answer": "A",
        "explanation": "The walrus operator := assigns y = x * 2 within the comprehension condition. When y > 6 (for x=4: 8, x=5: 10, x=6: 12), y is yielded into res, producing [8, 10, 12]."
    },
    {
        "id": 203,
        "topic": "Day 01: Structural Pattern Matching",
        "question": "In Python 3.10+, what does the following match/case statement output?",
        "code": 'command = ("move", 10, 20)\nmatch command:\n    case ("quit",):\n        res = "Exiting"\n    case ("move", x, y):\n        res = f"Moving to {x},{y}"\n    case _:\n        res = "Unknown"\nprint(res)',
        "options": [
            "A) Moving to 10,20",
            "B) Unknown",
            "C) Exiting",
            "D) SyntaxError"
        ],
        "answer": "A",
        "explanation": "Python's match/case unpacks the 3-element tuple into the pattern ('move', x, y), binding x=10 and y=20, producing 'Moving to 10,20'."
    },
    {
        "id": 204,
        "topic": "Day 01: IEEE-754 Floating Point Precision",
        "question": "What is the output of print(0.1 + 0.2 == 0.3, round(0.1 + 0.2, 2) == 0.3)?",
        "code": 'print(0.1 + 0.2 == 0.3, round(0.1 + 0.2, 2) == 0.3)',
        "options": [
            "A) True True",
            "B) False True",
            "C) True False",
            "D) False False"
        ],
        "answer": "B",
        "explanation": "Due to binary IEEE-754 floating point representation, 0.1 + 0.2 equals 0.30000000000000004, making 0.1 + 0.2 == 0.3 False. Rounding to 2 decimal places yields 0.3, so the rounded comparison is True."
    },
    {
        "id": 205,
        "topic": "Day 01: Starred Expression Unpacking",
        "question": "What is the output of the following extended iterable unpacking statement?",
        "code": 'first, *middle, last = [10, 20, 30, 40, 50]\nprint(first, middle, last)',
        "options": [
            "A) 10 [20, 30, 40] 50",
            "B) 10 (20, 30, 40) 50",
            "C) [10] [20, 30, 40] [50]",
            "D) ValueError"
        ],
        "answer": "A",
        "explanation": "Extended unpacking binds the first element to first (10), the last element to last (50), and collects all intermediate elements into a list: middle = [20, 30, 40]."
    },
    {
        "id": 206,
        "topic": "Day 02: Advanced String Formatting Specifier",
        "question": "What is the output of the formatted string f'{1234567.89:*>15,._2f}'?",
        "code": 'val = 1234567.89\nprint(f"{val:*>15,._2f}")',
        "options": [
            "A) ***1,234,567.89",
            "B) 1,234,567.89***",
            "C) **1,234,567.890",
            "D) 1234567.890000*"
        ],
        "answer": "A",
        "explanation": "The format specifier ':*>15,._2f' specifies: align right (>), pad with asterisk (*), total width 15, comma thousands separator (,), and 2 decimal places (.2f). '1,234,567.89' has length 12; padded to 15 chars gives '***1,234,567.89'."
    },
    {
        "id": 207,
        "topic": "Day 02: String Interning Mechanics",
        "question": "Under what circumstance does CPython automatically intern strings?",
        "code": None,
        "options": [
            "A) All strings regardless of length or characters are always interned",
            "B) Compile-time constants containing only ASCII letters, digits, and underscores (valid Python identifiers)",
            "C) Only strings read dynamically from user input()",
            "D) Strings containing spaces and emojis"
        ],
        "answer": "B",
        "explanation": "CPython automatically interns compile-time constant string literals that look like valid identifiers (alphanumeric + underscore). Dynamically constructed strings or those with special characters are not interned unless sys.intern() is explicitly called."
    },
    {
        "id": 208,
        "topic": "Day 02: str.casefold() vs str.lower()",
        "question": "Why is str.casefold() preferred over str.lower() when implementing caseless string matching?",
        "code": None,
        "options": [
            "A) casefold() runs 2x faster than lower()",
            "B) casefold() implements aggressive Unicode full case-folding (e.g. converting German 'ß' to 'ss'), enabling true language-agnostic matching",
            "C) casefold() strips punctuation as well",
            "D) lower() cannot handle ASCII capital letters"
        ],
        "answer": "B",
        "explanation": "casefold() is designed for aggressive Unicode caseless matching and handles characters like the German lowercase 'ß' (converting it to 'ss'), which lower() does not change."
    },
    {
        "id": 209,
        "topic": "Day 01: Short-Circuit Side Effects",
        "question": "What is the output of the following expression containing mutating side effects?",
        "code": 'nums = []\ndef check():\n    nums.append(1)\n    return False\nres = check() and check()\nprint(len(nums))',
        "options": [
            "A) 2",
            "B) 1",
            "C) 0",
            "D) False"
        ],
        "answer": "B",
        "explanation": "The first call to check() appends 1 and returns False. Because the 'and' operator short-circuits on the first falsy operand, the second check() is never invoked. len(nums) is 1."
    },
    {
        "id": 210,
        "topic": "Day 02: bytes vs bytearray",
        "question": "What is the key architectural difference between Python's bytes and bytearray types?",
        "code": None,
        "options": [
            "A) bytes is mutable, bytearray is immutable",
            "B) bytes is immutable, bytearray is mutable",
            "C) bytes stores Unicode, bytearray stores ASCII",
            "D) Both are completely immutable"
        ],
        "answer": "B",
        "explanation": "bytes objects are immutable sequences of single bytes (integers in 0-255). bytearray objects are mutable sequences of bytes supporting in-place modifications."
    },

    # Day 03 - 04: Advanced Data Structures & Memory (Q211 - Q225)
    {
        "id": 211,
        "topic": "Day 03: copy.deepcopy() Mechanics",
        "question": "Consider the following deepcopy code with cyclical references:\nimport copy\na = [1, 2]\na.append(a)\nb = copy.deepcopy(a)\nprint(b[2] is b, b[2] is a)\nWhat is the output?",
        "code": 'import copy\na = [1, 2]\na.append(a)\nb = copy.deepcopy(a)\nprint(b[2] is b, b[2] is a)',
        "options": [
            "A) True False",
            "B) True True",
            "C) False False",
            "D) RecursionError is raised"
        ],
        "answer": "A",
        "explanation": "copy.deepcopy maintains an internal memo dictionary mapping original objects to their copies to handle circular references. b[2] points to b itself (True) and not the original a (False)."
    },
    {
        "id": 212,
        "topic": "Day 04: Hashable Contract for Dictionary Keys",
        "question": "What is the required contract for two objects in Python to be treated as identical keys in a dictionary?",
        "code": None,
        "options": [
            "A) They must have the same memory address (id(a) == id(b))",
            "B) They must compare equal (a == b) and produce identical hash values (hash(a) == hash(b))",
            "C) They must share the same class definition",
            "D) They must both be strings"
        ],
        "answer": "B",
        "explanation": "Dictionary lookup checks hash(key) first to find the bucket, and then checks equality (key == target) to handle collisions. Identical keys require hash(a) == hash(b) and a == b."
    },
    {
        "id": 213,
        "topic": "Day 04: collections.defaultdict",
        "question": "What is the output of the following code using collections.defaultdict?",
        "code": 'from collections import defaultdict\nd = defaultdict(list)\nd["fruits"].append("apple")\nprint(d["vegetables"], d["fruits"])',
        "options": [
            "A) KeyError: 'vegetables'",
            "B) [] ['apple']",
            "C) None ['apple']",
            "D) [None] ['apple']"
        ],
        "answer": "B",
        "explanation": "When a missing key is accessed, defaultdict calls the default_factory callable (list()) to automatically create and insert an empty list []."
    },
    {
        "id": 214,
        "topic": "Day 04: collections.Counter Addition",
        "question": "What is the output of adding two Counter objects?",
        "code": 'from collections import Counter\nc1 = Counter(a=3, b=1)\nc2 = Counter(a=1, b=2, c=4)\nres = c1 + c2\nprint(res["a"], res["b"], res["c"])',
        "options": [
            "A) 3 1 4",
            "B) 4 3 4",
            "C) 3 2 4",
            "D) KeyError: 'c'"
        ],
        "answer": "B",
        "explanation": "Adding Counters sums corresponding item counts: a: 3+1=4, b: 1+2=3, c: 0+4=4. Output: 4 3 4."
    },
    {
        "id": 215,
        "topic": "Day 03: List Comprehension Scope in Python 3",
        "question": "What is the output of the following code regarding comprehension variable leakage?",
        "code": 'x = 100\nres = [x for x in range(3)]\nprint(x)',
        "options": [
            "A) 2",
            "B) 100",
            "C) 3",
            "D) NameError"
        ],
        "answer": "B",
        "explanation": "In Python 3, list comprehensions have their own local function-like scope. The loop variable x inside the comprehension does NOT leak into the outer scope. Outer x remains 100."
    },
    {
        "id": 216,
        "topic": "Day 04: Custom Class as Dict Key",
        "question": "What occurs when Point objects are used as dict keys in the following code?",
        "code": 'class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __hash__(self):\n        return hash((self.x, self.y))\n    def __eq__(self, other):\n        return (self.x, self.y) == (other.x, other.y)\nd = {Point(1, 2): "Origin"}\nprint(d.get(Point(1, 2)))',
        "options": [
            "A) None",
            "B) Origin",
            "C) TypeError: unhashable type: 'Point'",
            "D) KeyError"
        ],
        "answer": "B",
        "explanation": "Because Point implements both __hash__ and __eq__ based on (x, y), Point(1, 2) hashes to the same value and compares equal to the key in d, returning 'Origin'."
    },
    {
        "id": 217,
        "topic": "Day 04: Set Hash Collisions",
        "question": "What is the output of len({1, True, 1.0}) in Python?",
        "code": 's = {1, True, 1.0}\nprint(len(s))',
        "options": [
            "A) 3",
            "B) 1",
            "C) 2",
            "D) TypeError"
        ],
        "answer": "B",
        "explanation": "In Python, 1 == True == 1.0, and hash(1) == hash(True) == hash(1.0). Since sets deduplicate based on hash equality and value equality, only one element remains. len is 1."
    },
    {
        "id": 218,
        "topic": "Day 03: collections.namedtuple",
        "question": "What is the primary characteristic of collections.namedtuple instances?",
        "code": 'from collections import namedtuple\nTask = namedtuple("Task", ["id", "title"])\nt = Task(1, "Fix bug")',
        "options": [
            "A) They are mutable like dictionaries",
            "B) They are immutable tuples with named field access and zero per-instance dict memory overhead",
            "C) They can only store string values",
            "D) They do not support indexing by integer position"
        ],
        "answer": "B",
        "explanation": "namedtuple creates a tuple subclass that allows attribute access by field name (t.title) as well as index access (t[1]), while retaining the immutability and compact memory footprint of tuples."
    },
    {
        "id": 219,
        "topic": "Day 03: collections.deque Performance",
        "question": "Why is collections.deque significantly faster than a Python list for implementing queues?",
        "code": None,
        "options": [
            "A) deque compresses elements using gzip",
            "B) deque provides O(1) amortized append and pop operations from both ends, whereas list.pop(0) and list.insert(0, v) are O(n)",
            "C) deque uses multi-threading automatically",
            "D) deque is implemented in assembly"
        ],
        "answer": "B",
        "explanation": "A Python list is a contiguous array where inserting or popping at index 0 requires shifting all remaining n elements (O(n)). deque is a doubly-linked list of blocks with O(1) appends and pops at both ends."
    },
    {
        "id": 220,
        "topic": "Day 04: Dictionary Keys Union in Python 3",
        "question": "What is the output of the set operation on dictionary keys?",
        "code": 'd1 = {"a": 1, "b": 2}\nd2 = {"b": 3, "c": 4}\nprint(d1.keys() & d2.keys())',
        "options": [
            "A) {'b'}",
            "B) [('b', 2), ('b', 3)]",
            "C) {'b': 2}",
            "D) TypeError: unhashable type: 'dict_keys'"
        ],
        "answer": "A",
        "explanation": "dict.keys() returns a dictionary view that behaves like a set (set-like view), supporting set operations like & (intersection). The common key is {'b'}."
    },

    # Day 05: Advanced Functions, Closures, Decorators & RegEx (Q221 - Q240)
    {
        "id": 221,
        "topic": "Day 05: Closure Late Binding Trap",
        "question": "Consider the following code creating a list of lambda closures:\nmultipliers = [lambda x: x * i for i in range(4)]\nresults = [f(2) for f in multipliers]\nprint(results)\nWhat is the output?",
        "code": 'multipliers = [lambda x: x * i for i in range(4)]\nresults = [f(2) for f in multipliers]\nprint(results)',
        "options": [
            "A) [0, 2, 4, 6]",
            "B) [6, 6, 6, 6]",
            "C) [0, 1, 2, 3]",
            "D) [8, 8, 8, 8]"
        ],
        "answer": "B",
        "explanation": "Python closures bind variables by reference (late binding), not by value. When the lambdas are executed, the loop has completed and i is 3 for all of them. f(2) = 2 * 3 = 6 for each function: [6, 6, 6, 6]."
    },
    {
        "id": 222,
        "topic": "Day 05: Fixing Closure Late Binding",
        "question": "How do you correctly fix late binding in the closure loop so that each lambda captures the loop's current index value?",
        "code": None,
        "options": [
            "A) [lambda x: x * copy(i) for i in range(4)]",
            "B) [lambda x, i=i: x * i for i in range(4)]",
            "C) [lambda x: x * global(i) for i in range(4)]",
            "D) [lambda x: x * nonlocal(i) for i in range(4)]"
        ],
        "answer": "B",
        "explanation": "Using a default parameter 'i=i' forces Python to evaluate and bind the current value of i at lambda definition time into a local parameter."
    },
    {
        "id": 223,
        "topic": "Day 05: functools.wraps Role",
        "question": "Why is @functools.wraps(fn) used inside custom function decorators?",
        "code": 'from functools import wraps\ndef my_dec(f):\n    @wraps(f)\n    def wrapper(*args, **kwargs):\n        return f(*args, **kwargs)\n    return wrapper',
        "options": [
            "A) To make the decorated function run asynchronously",
            "B) To copy over original metadata such as __name__, __doc__, and __annotations__ to wrapper",
            "C) To prevent the decorator from executing more than once",
            "D) To enforce type validation on arguments"
        ],
        "answer": "B",
        "explanation": "Without @functools.wraps, decorated functions lose their identity: __name__ becomes 'wrapper' and __doc__ is erased. wraps restores the original function's introspection attributes."
    },
    {
        "id": 224,
        "topic": "Day 05: Decorator with Arguments (Decorator Factory)",
        "question": "How many levels of nested functions are required to implement a decorator that accepts parameters (e.g. @repeat(num_times=3))?",
        "code": None,
        "options": [
            "A) 1 level",
            "B) 2 levels",
            "C) 3 levels",
            "D) 4 levels"
        ],
        "answer": "C",
        "explanation": "A decorator taking arguments requires 3 levels: (1) outer factory accepting decorator parameters, (2) middle decorator accepting the target function, and (3) inner wrapper executing logic and arguments."
    },
    {
        "id": 225,
        "topic": "Day 05: Multiple Decorator Stacking Order",
        "question": "What is the execution order of stacked decorators?\n@dec1\n@dec2\ndef func(): pass",
        "code": '@dec1\n@dec2\ndef func(): pass',
        "options": [
            "A) dec1 wraps func first, then dec2 wraps dec1",
            "B) Applied from bottom to top: func = dec1(dec2(func)); during invocation, dec1's wrapper runs before dec2's wrapper",
            "C) Executed randomly based on hash seed",
            "D) Raises a SyntaxError"
        ],
        "answer": "B",
        "explanation": "Decorators are applied bottom-up: dec2 wraps func, then dec1 wraps the result: dec1(dec2(func)). When calling func(), execution flows from outermost (dec1) to innermost (dec2)."
    },
    {
        "id": 226,
        "topic": "Day 05: functools.lru_cache",
        "question": "What does the @functools.lru_cache decorator do when applied to a recursive function like fibonacci(n)?",
        "code": 'from functools import lru_cache\n@lru_cache(maxsize=128)\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)',
        "options": [
            "A) Limits recursion depth to 128 calls",
            "B) Memoizes function return values based on input arguments, turning an O(2^n) exponential function into O(n) linear time",
            "C) Runs the function in parallel across 128 CPU cores",
            "D) Clears RAM when memory exceeds 128 MB"
        ],
        "answer": "B",
        "explanation": "lru_cache implements Least Recently Used caching (memoization), storing computed outputs mapped to argument hashes and avoiding redundant recursive calculations."
    },
    {
        "id": 227,
        "topic": "Day 05: RegEx Lookaround Assertions",
        "question": "What does the regular expression r'\\d+(?=\\s*USD)' match in 'Cost is 450 USD and 300 EUR'?",
        "code": 'import re\ntext = "Cost is 450 USD and 300 EUR"\nmatches = re.findall(r"\\d+(?=\\s*USD)", text)\nprint(matches)',
        "options": [
            "A) ['450 USD']",
            "B) ['450']",
            "C) ['450', '300']",
            "D) []"
        ],
        "answer": "B",
        "explanation": "(?=\\s*USD) is a positive lookahead. It asserts that \\d+ is followed by USD without consuming USD into the matched string. Result: ['450']."
    },
    {
        "id": 228,
        "topic": "Day 05: RegEx Negative Lookbehind",
        "question": "What is matched by r'(?<!\\$)\\b\\d+\\b' in '$100 and 200'?",
        "code": 'import re\ntext = "$100 and 200"\nmatches = re.findall(r"(?<!\\$)\\b\\d+\\b", text)\nprint(matches)',
        "options": [
            "A) ['100']",
            "B) ['200']",
            "C) ['100', '200']",
            "D) ['$100', '200']"
        ],
        "answer": "B",
        "explanation": "(?<!\\$) is a negative lookbehind asserting that the number is NOT preceded by a dollar sign. 100 is preceded by $, so it is ignored. Output: ['200']."
    },
    {
        "id": 229,
        "topic": "Day 05: RegEx Named Capturing Groups",
        "question": "How do you extract a named group 'year' from a regex match object?",
        "code": 'import re\nm = re.match(r"(?P<year>\\d{4})-(?P<month>\\d{2})", "2026-10")\nprint(m.group("year"))',
        "options": [
            "A) m.group('year')",
            "B) m['year']",
            "C) m.year",
            "D) m.named('year')"
        ],
        "answer": "A",
        "explanation": "Named capturing groups (?P<name>...) are accessed by passing the group name string to match.group('name') or via match.groupdict()."
    },
    {
        "id": 230,
        "topic": "Day 05: Modifying Global vs UnboundLocalError",
        "question": "What is the result of running the following code?",
        "code": 'count = 10\ndef increment():\n    count += 1\nincrement()',
        "options": [
            "A) count becomes 11",
            "B) UnboundLocalError: cannot access local variable 'count' where it is not associated with a value",
            "C) NameError: count is undefined",
            "D) count remains 10"
        ],
        "answer": "B",
        "explanation": "Because count += 1 assigns to count, Python marks count as a local variable throughout the entire function body. Referencing it before the assignment triggers UnboundLocalError."
    },

    # Day 06: Advanced OOP, Metaprogramming, MRO & Dunders (Q231 - Q250)
    {
        "id": 231,
        "topic": "Day 06: MRO & Diamond Inheritance",
        "question": "Consider the following classic diamond inheritance hierarchy:\nclass A:\n    def ping(self): return 'A'\nclass B(A):\n    def ping(self): return 'B'\nclass C(A):\n    def ping(self): return 'C'\nclass D(B, C):\n    pass\nWhat does D().ping() return?",
        "code": 'class A:\n    def ping(self): return "A"\nclass B(A):\n    def ping(self): return "B"\nclass C(A):\n    def ping(self): return "C"\nclass D(B, C):\n    pass\nprint(D().ping())',
        "options": [
            "A) A",
            "B) B",
            "C) C",
            "D) AttributeError"
        ],
        "answer": "B",
        "explanation": "According to Python's C3 Linearization algorithm, D's MRO is [D, B, C, A, object]. Looking up ping() finds B's implementation first, returning 'B'."
    },
    {
        "id": 232,
        "topic": "Day 06: Cooperative super() in Diamond Hierarchy",
        "question": "What is the output of D().process() in the following cooperative multiple inheritance code?",
        "code": 'class A:\n    def process(self):\n        return ["A"]\nclass B(A):\n    def process(self):\n        return ["B"] + super().process()\nclass C(A):\n    def process(self):\n        return ["C"] + super().process()\nclass D(B, C):\n    def process(self):\n        return ["D"] + super().process()\nprint(D().process())',
        "options": [
            "A) ['D', 'B', 'A']",
            "B) ['D', 'B', 'C', 'A']",
            "C) ['D', 'B', 'A', 'C', 'A']",
            "D) ['D', 'C', 'B', 'A']"
        ],
        "answer": "B",
        "explanation": "MRO for D is [D, B, C, A, object]. In B, super().process() resolves to the next class in D's MRO, which is C! C calls super() to A. Output: ['D', 'B', 'C', 'A']."
    },
    {
        "id": 233,
        "topic": "Day 06: __new__ vs __init__ (Singleton Pattern)",
        "question": "What is the fundamental difference between __new__ and __init__?",
        "code": None,
        "options": [
            "A) __init__ creates the instance; __new__ initializes it",
            "B) __new__ is a static method responsible for allocating and returning a new instance; __init__ is called on that newly returned instance to initialize state",
            "C) __new__ is only used for classes without inheritance",
            "D) They are completely interchangeable"
        ],
        "answer": "B",
        "explanation": "__new__(cls) allocates the raw memory and returns the newly created object. __init__(self) is then invoked with that instance to set initial attribute values."
    },
    {
        "id": 234,
        "topic": "Day 06: Memory Optimization with __slots__",
        "question": "What happens when a class defines __slots__ = ('name', 'age')?",
        "code": 'class Person:\n    __slots__ = ("name", "age")',
        "options": [
            "A) The class suppresses the creation of an instance __dict__, saving substantial memory and restricting instance attributes strictly to 'name' and 'age'",
            "B) The class attributes become read-only constants",
            "C) The class can only be instantiated twice",
            "D) The class can only inherit from tuple"
        ],
        "answer": "A",
        "explanation": "__slots__ replaces the dynamic per-instance __dict__ with fixed-size descriptor arrays, significantly reducing memory consumption and preventing arbitrary attribute assignment."
    },
    {
        "id": 235,
        "topic": "Day 06: Abstract Base Classes (abc.ABC)",
        "question": "What occurs if a subclass inherits from an ABC containing an @abstractmethod but fails to implement that method?",
        "code": 'from abc import ABC, abstractmethod\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): pass\nclass Square(Shape):\n    pass\ns = Square()',
        "options": [
            "A) Square instantiates normally, but calling area() raises NotImplementedError",
            "B) TypeError: Can't instantiate abstract class Square without an implementation for abstract method 'area'",
            "C) SyntaxError at class definition time",
            "D) s becomes None"
        ],
        "answer": "B",
        "explanation": "Python strictly prevents instantiation of any subclass that does not override all abstract methods, raising a TypeError during instantiation."
    },
    {
        "id": 236,
        "topic": "Day 06: Dunder __call__ Method",
        "question": "What does defining __call__ on a class allow instances of that class to do?",
        "code": 'class Multiplier:\n    def __init__(self, factor):\n        self.factor = factor\n    def __call__(self, val):\n        return self.factor * val\nm = Multiplier(5)\nprint(m(10))',
        "options": [
            "A) It allows instances to be invoked like regular functions: m(10)",
            "B) It automatically calls the garbage collector",
            "C) It allows instances to be used as list indices",
            "D) It converts the object to a string"
        ],
        "answer": "A",
        "explanation": "Implementing __call__ makes an instance callable like a standard function. m(10) calls m.__call__(10) = 5 * 10 = 50."
    },
    {
        "id": 237,
        "topic": "Day 06: Descriptor Protocol",
        "question": "Which three dunder methods constitute the Python Descriptor Protocol?",
        "code": None,
        "options": [
            "A) __init__, __new__, __del__",
            "B) __get__, __set__, __delete__",
            "C) __iter__, __next__, __len__",
            "D) __enter__, __exit__, __call__"
        ],
        "answer": "B",
        "explanation": "The Descriptor Protocol consists of __get__(self, instance, owner), __set__(self, instance, value), and __delete__(self, instance). It powers properties, methods, and classmethods."
    },
    {
        "id": 238,
        "topic": "Day 06: Metaclass Definition",
        "question": "In Python, what is a metaclass?",
        "code": None,
        "options": [
            "A) A class that cannot be inherited",
            "B) A class whose instances are themselves classes (a class that defines how a class behaves)",
            "C) A module containing only abstract methods",
            "D) The base class for all C-extensions"
        ],
        "answer": "B",
        "explanation": "A metaclass is a class whose instances are classes. In Python, the default metaclass for all classes is 'type'."
    },
    {
        "id": 239,
        "topic": "Day 06: Context Manager Protocol (__enter__ and __exit__)",
        "question": "What must the __exit__(self, exc_type, exc_val, exc_tb) method return to suppress an exception raised inside the 'with' block?",
        "code": None,
        "options": [
            "A) None",
            "B) True",
            "C) False",
            "D) A string containing the error message"
        ],
        "answer": "B",
        "explanation": "If __exit__ returns True (or a truthy value), Python swallows the exception and continues execution after the with block without propagating it."
    },
    {
        "id": 240,
        "topic": "Day 06: Dunder __getitem__ and Iteration",
        "question": "What happens if an object implements __getitem__ and __len__ but NOT __iter__ when passed to a 'for' loop?",
        "code": 'class CustomSeq:\n    def __len__(self): return 3\n    def __getitem__(self, idx):\n        if idx >= 3: raise IndexError\n        return idx * 10\nprint(list(CustomSeq()))',
        "options": [
            "A) TypeError: 'CustomSeq' object is not iterable",
            "B) Python falls back to old-style sequence iteration, calling __getitem__ starting at index 0 until IndexError: [0, 10, 20]",
            "C) An infinite loop occurs",
            "D) Raises AttributeError"
        ],
        "answer": "B",
        "explanation": "If __iter__ is not implemented, Python attempts to iterate by calling __getitem__ with integer indices 0, 1, 2... until an IndexError is raised, yielding [0, 10, 20]."
    },

    # Day 07: Advanced File Handling, Serialization & Database (Q241 - Q255)
    {
        "id": 241,
        "topic": "Day 07: File seek() with os.SEEK_END",
        "question": "What does f.seek(-5, os.SEEK_END) do on a file opened in 'rb' mode?",
        "code": None,
        "options": [
            "A) Moves the cursor 5 bytes before the start of the file",
            "B) Positions the file cursor 5 bytes before the end of the file",
            "C) Deletes the last 5 bytes of the file",
            "D) Raises an OSError in binary mode"
        ],
        "answer": "B",
        "explanation": "os.SEEK_END (value 2) references the end of the file. A negative offset moves the pointer backward from the EOF."
    },
    {
        "id": 242,
        "topic": "Day 07: Custom JSONEncoder",
        "question": "How do you serialize a Python datetime object to JSON using json.dumps()?",
        "code": None,
        "options": [
            "A) json.dumps(dt, enable_dates=True)",
            "B) Provide a custom serializer via the 'default' parameter: json.dumps(dt, default=str)",
            "C) datetime objects are natively JSON serializable by default",
            "D) json.dumps(dt, format='%Y-%m-%d')"
        ],
        "answer": "B",
        "explanation": "Standard json does not serialize datetime objects natively. Passing default=str or subclassing json.JSONEncoder converts unsupported objects."
    },
    {
        "id": 243,
        "topic": "Day 07: Pickle Security Vulnerability",
        "question": "Why is unpickling data received from an untrusted client or network source considered a critical security vulnerability?",
        "code": None,
        "options": [
            "A) It may contain malformed characters that crash the python parser",
            "B) Pickle bytecode can execute arbitrary Python/system commands during deserialization via the __reduce__ method",
            "C) Pickle files corrupt the local hard drive",
            "D) Pickle exposes database passwords"
        ],
        "answer": "B",
        "explanation": "pickle is not secure against erroneous or maliciously constructed data. The __reduce__ protocol allows pickled data to construct and execute arbitrary OS commands (e.g. os.system) upon unpickling."
    },
    {
        "id": 244,
        "topic": "Day 07: SQLite sqlite3.Row Factory",
        "question": "What is the benefit of setting conn.row_factory = sqlite3.Row in Python's sqlite3 module?",
        "code": 'conn.row_factory = sqlite3.Row\ncursor = conn.cursor()\nrow = cursor.execute("SELECT id, name FROM users").fetchone()',
        "options": [
            "A) Enables accessing returned row columns by name as well as index (e.g. row['name'] and row[1])",
            "B) Encrypts database rows on disk",
            "C) Makes queries run in separate threads",
            "D) Automatically converts rows to pandas DataFrame"
        ],
        "answer": "A",
        "explanation": "sqlite3.Row provides a highly optimized dictionary-like interface, allowing column access both by case-insensitive column name and by integer index."
    },
    {
        "id": 245,
        "topic": "Day 07: SQLite Connection as Context Manager",
        "question": "When an active sqlite3 connection is used as a context manager 'with conn:', what happens upon exiting the block?",
        "code": 'with conn:\n    conn.execute("INSERT INTO logs VALUES (?)", ("Event",))',
        "options": [
            "A) The database connection is closed automatically",
            "B) The transaction is committed automatically if no exceptions occurred, or rolled back if an exception was raised (the connection remains OPEN)",
            "C) The database file is deleted",
            "D) All tables are locked indefinitely"
        ],
        "answer": "B",
        "explanation": "Using 'with conn:' manages the transaction (commits on success, rolls back on exception). It does NOT close the connection; conn.close() must still be called separately."
    },
    {
        "id": 246,
        "topic": "Day 07: In-Memory SQLite Database",
        "question": "How do you create a fast, volatile SQLite database entirely in RAM in Python?",
        "code": None,
        "options": [
            "A) sqlite3.connect('temp.db')",
            "B) sqlite3.connect(':memory:')",
            "C) sqlite3.connect(ram=True)",
            "D) sqlite3.in_memory()"
        ],
        "answer": "B",
        "explanation": "Passing ':memory:' as the database path opens a private, pure-RAM database that exists only as long as the connection is open."
    },
    {
        "id": 247,
        "topic": "Day 07: contextlib.@contextmanager",
        "question": "What does a generator function decorated with @contextmanager yield to the 'as' target of a 'with' statement?",
        "code": 'from contextlib import contextmanager\n@contextmanager\ndef open_resource():\n    res = "Active"\n    try:\n        yield res\n    finally:\n        print("Closed")',
        "options": [
            "A) The generator iterator object itself",
            "B) The single value produced by the yield statement (res)",
            "C) A tuple of all variables in scope",
            "D) None"
        ],
        "answer": "B",
        "explanation": "The value yielded by the generator is passed to the 'as' variable in the 'with' statement. Any cleanup code in finally runs when the with block terminates."
    },
    {
        "id": 248,
        "topic": "Day 07: io.StringIO vs io.BytesIO",
        "question": "What is the difference between io.StringIO and io.BytesIO in Python?",
        "code": None,
        "options": [
            "A) io.StringIO operates as an in-memory stream for text (str); io.BytesIO operates as an in-memory stream for binary data (bytes)",
            "B) io.StringIO writes to disk, io.BytesIO writes to network",
            "C) Both only handle JSON data",
            "D) They are deprecated aliases for open()"
        ],
        "answer": "A",
        "explanation": "io.StringIO provides an in-memory file-like buffer for strings (unicode text), while io.BytesIO provides an in-memory buffer for raw bytes."
    },
    {
        "id": 249,
        "topic": "Day 07: csv.writer lineterminator Parameter",
        "question": "On Windows systems, why is it critical to pass newline='' when opening a CSV file with open() for csv.writer?",
        "code": 'with open("data.csv", "w", newline="", encoding="utf-8") as f:\n    w = csv.writer(f)',
        "options": [
            "A) To prevent csv.writer from producing double carriage returns (\\r\\r\\n) causing extra blank rows",
            "B) Windows throws a PermissionError without newline=''",
            "C) To allow binary data inside CSV",
            "D) To enforce UTF-16 encoding"
        ],
        "answer": "A",
        "explanation": "By default, csv.writer terminates rows with '\\r\\n'. If open() does not specify newline='', Python's universal newline translation replaces '\\n' with '\\r\\n', creating '\\r\\r\\n' (blank lines between rows)."
    },
    {
        "id": 250,
        "topic": "Day 07: SQLite Executemany Performance",
        "question": "Why is cursor.executemany(sql, seq_of_params) preferred over looping cursor.execute(sql, params) in a Python for-loop?",
        "code": None,
        "options": [
            "A) It skips data validation",
            "B) It batches parameter execution, reducing query compilation overhead and context switching across the Python/C DB-API boundary",
            "C) It disables database constraints",
            "D) It converts SQLite into PostgreSQL"
        ],
        "answer": "B",
        "explanation": "executemany() prepares the SQL statement once and executes it across all tuples in batch, significantly improving performance."
    },

    # Day 08: Advanced Iterators, Coroutines & Generators (Q251 - Q260)
    {
        "id": 251,
        "topic": "Day 08: Bidirectional Generator .send()",
        "question": "What is the output of the following generator utilizing the .send() method?",
        "code": 'def accumulator():\n    total = 0\n    while True:\n        val = yield total\n        if val is None: break\n        total += val\ngen = accumulator()\nnext(gen)\nprint(gen.send(10), gen.send(20))',
        "options": [
            "A) 10 20",
            "B) 10 30",
            "C) 0 10",
            "D) TypeError"
        ],
        "answer": "B",
        "explanation": "next(gen) advances to the first yield total (0). gen.send(10) sets val=10, total becomes 10, yields 10. gen.send(20) sets val=20, total becomes 30, yields 30. Output: 10 30."
    },
    {
        "id": 252,
        "topic": "Day 08: Priming a Generator Coroutine",
        "question": "Why must next(gen) or gen.send(None) be called on a generator before sending any non-None value with gen.send(value)?",
        "code": None,
        "options": [
            "A) Python raises TypeError: can't send non-None value to a just-started generator",
            "B) It clears the memory buffer",
            "C) It establishes a TCP socket",
            "D) It is an optional best practice that has no runtime effect"
        ],
        "answer": "A",
        "explanation": "A newly created generator has not yet reached its first yield expression. Calling send(val) with a non-None value before the generator has yielded raises TypeError."
    },
    {
        "id": 253,
        "topic": "Day 08: Generator .close() Method",
        "question": "What exception is raised inside a suspended generator when .close() is called on it?",
        "code": 'gen.close()',
        "options": [
            "A) StopIteration",
            "B) GeneratorExit",
            "C) RuntimeError",
            "D) SystemExit"
        ],
        "answer": "B",
        "explanation": "Calling gen.close() raises a GeneratorExit exception at the point where the generator was suspended, allowing try-finally cleanup blocks to execute."
    },
    {
        "id": 254,
        "topic": "Day 08: yield from Return Value",
        "question": "What is the value of 'res' in the following sub-generator delegation code?",
        "code": 'def sub_gen():\n    yield 1\n    yield 2\n    return "COMPLETED"\ndef main_gen():\n    res = yield from sub_gen()\n    yield res\nprint(list(main_gen()))',
        "options": [
            "A) [1, 2]",
            "B) [1, 2, 'COMPLETED']",
            "C) ['COMPLETED']",
            "D) [1, 2, StopIteration]"
        ],
        "answer": "B",
        "explanation": "yield from yields each item from sub_gen (1, 2). When sub_gen returns 'COMPLETED' (carried via StopIteration.value), that return value is assigned to res. main_gen then yields res, resulting in [1, 2, 'COMPLETED']."
    },
    {
        "id": 255,
        "topic": "Day 08: itertools.islice with Generators",
        "question": "What is the output of taking a slice from an infinite generator using itertools.islice?",
        "code": 'import itertools\ndef count_from(n):\n    while True:\n        yield n\n        n += 2\nsliced = list(itertools.islice(count_from(10), 3))\nprint(sliced)',
        "options": [
            "A) [10, 12, 14]",
            "B) [10, 11, 12]",
            "C) [12, 14, 16]",
            "D) Infinite loop"
        ],
        "answer": "A",
        "explanation": "itertools.islice lazily extracts the first 3 items from the generator without trying to evaluate the infinite sequence to completion: [10, 12, 14]."
    },
    {
        "id": 256,
        "topic": "Day 08: inspect.isgeneratorfunction",
        "question": "How does the Python runtime determine if a function is a generator function?",
        "code": None,
        "options": [
            "A) By checking if it has a @generator decorator",
            "B) By the presence of the 'yield' keyword anywhere in its compiled code object flags (CO_GENERATOR)",
            "C) By checking its return type annotation",
            "D) By checking if its name starts with 'gen_'"
        ],
        "answer": "B",
        "explanation": "During compilation to bytecode, if the function body contains the yield keyword, the code object's flags are marked with CO_GENERATOR."
    },
    {
        "id": 257,
        "topic": "Day 08: Custom Iterable Class",
        "question": "What is the difference between an Iterable and an Iterator in Python?",
        "code": None,
        "options": [
            "A) An Iterable implements __iter__ returning an iterator; an Iterator implements __next__ (and __iter__ returning self)",
            "B) They are identical concepts",
            "C) Iterators can only be looped over once, while Iterables can never be looped over",
            "D) An Iterable is always a generator"
        ],
        "answer": "A",
        "explanation": "An iterable is any object capable of returning its members one at a time (implements __iter__). An iterator is the stateful stream object that actually produces values on __next__()."
    },
    {
        "id": 258,
        "topic": "Day 08: StopIteration Value Attribute",
        "question": "When a generator function executes 'return 42', where does the value 42 go?",
        "code": 'def my_gen():\n    yield 1\n    return 42\ng = my_gen()\nnext(g)\ntry:\n    next(g)\nexcept StopIteration as e:\n    print(e.value)',
        "options": [
            "A) It is lost and discarded",
            "B) It is stored in the StopIteration exception's .value attribute",
            "C) It is printed to stderr",
            "D) Return statements with values are illegal inside generators"
        ],
        "answer": "B",
        "explanation": "In Python 3.3+, a value returned from a generator is attached to the .value attribute of the StopIteration exception that terminates the generator."
    },
    {
        "id": 259,
        "topic": "Day 08: Generator Expression Re-use",
        "question": "What is the output of attempting to iterate over an already exhausted generator expression a second time?",
        "code": 'gen = (x for x in [1, 2])\nlist1 = list(gen)\nlist2 = list(gen)\nprint(list1, list2)',
        "options": [
            "A) [1, 2] [1, 2]",
            "B) [1, 2] []",
            "C) [1, 2] [None]",
            "D) StopIteration is raised"
        ],
        "answer": "B",
        "explanation": "Generators are single-use iterators. Once exhausted, subsequent iterations immediately return an empty result without resetting: [1, 2] []."
    },
    {
        "id": 260,
        "topic": "Day 08: Exception Handling Hierarchy",
        "question": "Why does catching 'except Exception:' NOT intercept a generator's GeneratorExit or keyboard interrupts?",
        "code": None,
        "options": [
            "A) GeneratorExit and KeyboardInterrupt inherit directly from BaseException, not Exception",
            "B) They are not Python exceptions",
            "C) They can only be caught using try-finally",
            "D) Python suppresses them automatically"
        ],
        "answer": "A",
        "explanation": "In Python's exception hierarchy, BaseException is the root. SystemExit, KeyboardInterrupt, and GeneratorExit inherit directly from BaseException so standard 'except Exception' handlers do not accidentally catch them."
    },

    # Day 09 - 10: Advanced Web Architecture, REST & Scraping (Q261 - Q280)
    {
        "id": 261,
        "topic": "Day 09: Flask Application vs Request Context",
        "question": "What is the difference between Flask's Application Context ('current_app', 'g') and Request Context ('request', 'session')?",
        "code": None,
        "options": [
            "A) Application context is tied to the running application configuration and shared state; Request context tracks data specific to an individual incoming HTTP request",
            "B) Application context is for client side; Request context is for server side",
            "C) Request context only exists for POST requests",
            "D) There is no distinction in Flask"
        ],
        "answer": "A",
        "explanation": "Flask splits context into two stacks: Application Context (manages app-level objects like db configs and 'g') and Request Context (manages request-specific info like URLs, headers, and form data)."
    },
    {
        "id": 262,
        "topic": "Day 09: Flask Blueprints Purpose",
        "question": "What is the primary architectural purpose of Flask Blueprints?",
        "code": None,
        "options": [
            "A) To generate CSS blueprints for front-end styling",
            "B) To organize a large application into reusable, modular sub-components with their own URL prefixes, templates, and static directories",
            "C) To manage database migrations",
            "D) To compile Flask into C code"
        ],
        "answer": "B",
        "explanation": "Blueprints enable modular architecture by allowing route handlers, templates, and static folders to be grouped and registered under specific URL prefixes."
    },
    {
        "id": 263,
        "topic": "Day 10: REST PUT vs PATCH Semantics",
        "question": "According to standard REST conventions, what is the exact semantic difference between HTTP PUT and HTTP PATCH?",
        "code": None,
        "options": [
            "A) PUT and PATCH are completely identical",
            "B) PUT replaces the entire target resource with the uploaded representation; PATCH applies partial modifications/deltas to the existing resource",
            "C) PUT is for creation only; PATCH is for deletion",
            "D) PATCH is idempotent; PUT is never idempotent"
        ],
        "answer": "B",
        "explanation": "PUT performs complete resource replacement (idempotent). PATCH applies a partial update/delta to modify only specific fields."
    },
    {
        "id": 264,
        "topic": "Day 10: HTTP 401 vs 403 Status Codes",
        "question": "What is the precise difference between HTTP 401 Unauthorized and HTTP 403 Forbidden?",
        "code": None,
        "options": [
            "A) 401 means Authentication is required or credentials failed; 403 means the user is authenticated, but lacks Authorization (permission) to access the resource",
            "B) 401 is for server errors; 403 is for client errors",
            "C) 401 is for GET requests; 403 is for POST requests",
            "D) They are synonyms"
        ],
        "answer": "A",
        "explanation": "401 Unauthorized indicates authentication is missing or invalid. 403 Forbidden indicates the identity is known, but access is refused due to insufficient permissions."
    },
    {
        "id": 265,
        "topic": "Day 10: Flask Custom Error Handler",
        "question": "How do you register a custom 404 JSON error response in Flask?",
        "code": None,
        "options": [
            "A) @app.catch(404)",
            "B) @app.errorhandler(404)\ndef not_found(e):\n    return jsonify(error='Not Found'), 404",
            "C) @app.route('/404')",
            "D) @app.handle_error(404)"
        ],
        "answer": "B",
        "explanation": "@app.errorhandler(404) registers a function to intercept HTTP 404 exceptions and return a custom response and status code."
    },
    {
        "id": 266,
        "topic": "Day 10: BeautifulSoup CSS Selector select()",
        "question": "In BeautifulSoup, what is returned by soup.select('div.card > a.btn[href^=\"https\"]')?",
        "code": None,
        "options": [
            "A) The first matching element as a Tag object",
            "B) A list of all Tag objects matching the CSS selector (direct anchor children of div.card with class 'btn' starting with https)",
            "C) A boolean indicating whether such elements exist",
            "D) An iterator of strings"
        ],
        "answer": "B",
        "explanation": "soup.select() evaluates CSS selectors and returns a list of all matching Tag elements."
    },
    {
        "id": 267,
        "topic": "Day 10: Web Scraping User-Agent Header",
        "question": "Why is it often necessary to supply a custom 'User-Agent' header when sending HTTP GET requests using Python's requests library?",
        "code": 'headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}\nresp = requests.get(url, headers=headers)',
        "options": [
            "A) requests will not compile without headers",
            "B) Many web servers block or return HTTP 403 to requests with the default 'python-requests/x.x' User-Agent to prevent bot scraping",
            "C) To enable SSL certificate validation",
            "D) To compress the returned HTML response"
        ],
        "answer": "B",
        "explanation": "Web servers frequently reject requests bearing the default 'python-requests' User-Agent. Spoofing a standard browser User-Agent avoids bot blocking."
    },
    {
        "id": 268,
        "topic": "Day 10: requests.Session() Connection Pooling",
        "question": "What is the primary performance benefit of using a requests.Session() object when scraping multiple pages from the same host?",
        "code": 'with requests.Session() as s:\n    for url in urls:\n        resp = s.get(url)',
        "options": [
            "A) It automatically executes JavaScript",
            "B) It persists cookies and reuses the underlying TCP connection (HTTP Keep-Alive), eliminating repeated TCP and TLS handshakes",
            "C) It bypasses CAPTCHA challenges automatically",
            "D) It multithreads the network socket"
        ],
        "answer": "B",
        "explanation": "requests.Session() uses urllib3 connection pooling, persisting cookies across requests and keeping TCP/TLS connections alive, dramatically speeding up consecutive requests."
    },
    {
        "id": 269,
        "topic": "Day 10: BeautifulSoup NavigableString vs Tag",
        "question": "What is the difference between soup.find('p') and soup.find('p').string?",
        "code": None,
        "options": [
            "A) find('p') returns a Tag object; .string returns a NavigableString containing the text",
            "B) Both return plain Python strings",
            "C) find('p').string returns an integer length",
            "D) find('p') returns an XML parser"
        ],
        "answer": "A",
        "explanation": "find('p') returns a bs4.element.Tag object representing the HTML node. .string extracts the inner content as a bs4.element.NavigableString."
    },
    {
        "id": 270,
        "topic": "Day 10: REST Architectural Constraints",
        "question": "Which of the following is NOT one of Roy Fielding's 6 foundational REST architectural constraints?",
        "code": None,
        "options": [
            "A) Statelessness",
            "B) Client-Server Separation",
            "C) Cacheability",
            "D) Mandatory Object-Relational Mapping (ORM)"
        ],
        "answer": "D",
        "explanation": "The 6 REST constraints are: Client-Server, Stateless, Cacheable, Uniform Interface, Layered System, and Code on Demand. ORM is an internal implementation pattern, not a REST constraint."
    },

    # Day 10 - 11: Advanced NumPy, Pandas & Data Visualization (Q271 - Q300)
    {
        "id": 271,
        "topic": "Day 10: NumPy 3D Array Striding & Slicing",
        "question": "Given arr = np.arange(24).reshape((2, 3, 4)), what is the shape and the element sub[0, 0, 0] of the slice sub = arr[:, ::-1, 1:3]?",
        "code": 'import numpy as np\narr = np.arange(24).reshape((2, 3, 4))\nsub = arr[:, ::-1, 1:3]\nprint(sub.shape, sub[0, 0, 0])',
        "options": [
            "A) (2, 3, 2) and 9",
            "B) (2, 3, 2) and 1",
            "C) (2, 2, 2) and 9",
            "D) (2, 3, 3) and 8"
        ],
        "answer": "A",
        "explanation": "Axis 0 has length 2. Axis 1 is reversed (length 3). Axis 2 slices indices 1 and 2 (length 2). Shape is (2, 3, 2). sub[0, 0, 0] corresponds to original arr[0, 2, 1] (row index 2 from reverse, column 1): 2*4 + 1 = 9."
    },
    {
        "id": 272,
        "topic": "Day 10: NumPy View vs Copy Slicing",
        "question": "Unlike standard Python lists where slicing creates a shallow copy, what does basic slicing on a NumPy ndarray produce?",
        "code": 'a = np.array([1, 2, 3])\nb = a[1:]\nb[0] = 99\nprint(a[1])',
        "options": [
            "A) 2",
            "B) 99",
            "C) IndexError",
            "D) ValueError"
        ],
        "answer": "B",
        "explanation": "Basic slicing in NumPy creates a memory view (sharing the underlying data buffer), not a copy. Modifying elements in slice b modifies original array a (a[1] becomes 99)."
    },
    {
        "id": 273,
        "topic": "Day 10: NumPy Fancy Indexing creates Copy",
        "question": "What is the key difference between basic slicing and fancy indexing (integer array indexing) in NumPy?",
        "code": 'arr = np.array([10, 20, 30, 40])\nview = arr[1:3]\ncopy = arr[[1, 2]]',
        "options": [
            "A) Basic slicing returns a view; Fancy indexing always creates and returns a copy",
            "B) Both return views",
            "C) Fancy indexing is only for 1D arrays",
            "D) Basic slicing is slower than fancy indexing"
        ],
        "answer": "A",
        "explanation": "Fancy indexing (indexing via lists/arrays of integer indices or boolean masks) always allocates and returns a new array copy, unlike basic slicing which returns a view."
    },
    {
        "id": 274,
        "topic": "Day 11: Pandas SettingWithCopyWarning",
        "question": "What common code pattern triggers Pandas' SettingWithCopyWarning?",
        "code": 'df[df["status"] == "active"]["discount"] = 0.1',
        "options": [
            "A) Using string columns instead of categories",
            "B) Chained indexing assignment (e.g. df[cond]['col'] = val), because Pandas cannot guarantee whether df[cond] returned a view or a copy",
            "C) Calling df.dropna() without parameters",
            "D) Missing integer index"
        ],
        "answer": "B",
        "explanation": "Chained assignment performs two separate indexing operations. If the intermediate step is a copy, the assignment modifies a temporary object and is lost. Use df.loc[df['status'] == 'active', 'discount'] = 0.1 instead."
    },
    {
        "id": 275,
        "topic": "Day 11: Pandas MultiIndex Cross-Section (.xs)",
        "question": "What does df.xs('Lego', level='Company') do on a DataFrame with a MultiIndex on rows?",
        "code": None,
        "options": [
            "A) Deletes the 'Lego' company rows",
            "B) Returns a cross-section of data for the 'Lego' level key, dropping that level from the index by default",
            "C) Exports the rows to XML",
            "D) Resets the entire index to integers"
        ],
        "answer": "B",
        "explanation": ".xs() (cross-section) extracts rows or columns at a particular level of a MultiIndex."
    },
    {
        "id": 276,
        "topic": "Day 11: Pandas Performance Hierarchy",
        "question": "In what order of execution speed (fastest to slowest) do typical row-wise operations in Pandas rank?",
        "code": None,
        "options": [
            "A) Vectorized operations > df.apply() > df.itertuples() > df.iterrows()",
            "B) df.iterrows() > df.itertuples() > df.apply() > Vectorized operations",
            "C) df.apply() > Vectorized operations > df.iterrows() > df.itertuples()",
            "D) All have identical performance in Python 3"
        ],
        "answer": "A",
        "explanation": "Vectorized operations (executed in compiled C/SIMD) are fastest (~1x). df.apply() incurs Python function call overhead (~10-50x slower). df.itertuples() yields lightweight namedtuples (~100x slower). df.iterrows() instantiates a heavy Series object per row (~1000x slower)."
    },
    {
        "id": 277,
        "topic": "Day 11: Matplotlib Twin Axes (ax.twinx)",
        "question": "In Matplotlib, what does ax2 = ax.twinx() accomplish?",
        "code": 'fig, ax = plt.subplots()\nax2 = ax.twinx()',
        "options": [
            "A) Clones the plot side-by-side into two separate subplots",
            "B) Creates a second independent y-axis sharing the exact same x-axis on the same plot (dual-axis chart)",
            "C) Inverts the x-axis values",
            "D) Copies the figure to the clipboard"
        ],
        "answer": "B",
        "explanation": "ax.twinx() creates a new Axes object that shares the x-axis with ax, but displays its own independent scale on the right y-axis."
    },
    {
        "id": 278,
        "topic": "Day 11: Pandas Categorical Data Type",
        "question": "What is the primary benefit of converting a string column with few unique values to category dtype (df['City'].astype('category'))?",
        "code": None,
        "options": [
            "A) It allows values to be printed in bold",
            "B) Substantially reduced memory usage (storing integer codes instead of duplicate strings) and faster groupby computations",
            "C) It prevents null values",
            "D) It sorts the DataFrame automatically"
        ],
        "answer": "B",
        "explanation": "Categoricals store repetitive strings as compact integer category codes and a small unique lookup table, dramatically saving RAM and accelerating groupbys."
    },
    {
        "id": 279,
        "topic": "Day 10: NumPy Axis Parameter in Aggregation",
        "question": "What does np.sum(arr, axis=0) compute on a 2D array of shape (4, 5)?",
        "code": 'arr = np.ones((4, 5))\nres = np.sum(arr, axis=0)\nprint(res.shape)',
        "options": [
            "A) Sums along rows, collapsing axis 0 to return 5 column sums (shape (5,))",
            "B) Sums along columns, collapsing axis 1 to return 4 row sums (shape (4,))",
            "C) Sums all 20 elements to a scalar",
            "D) Shape (4, 5)"
        ],
        "answer": "A",
        "explanation": "Specifying axis=0 collapses the 0th dimension (rows) by summing down the columns, returning an array of shape (5,)."
    },
    {
        "id": 280,
        "topic": "Day 11: Matplotlib Object-Oriented API vs pyplot",
        "question": "Why is Matplotlib's Object-Oriented API ('fig, ax = plt.subplots(); ax.plot(...)') strongly recommended over the state-based pyplot API ('plt.plot(...)')?",
        "code": None,
        "options": [
            "A) pyplot is deprecated and removed in recent versions",
            "B) The Object-Oriented API provides explicit, isolated control over figures and axes without relying on implicit global state, avoiding cross-talk in multi-figure/multi-plot scripts",
            "C) The OO API executes 10x faster",
            "D) pyplot cannot draw bar charts"
        ],
        "answer": "B",
        "explanation": "The OO interface gives direct access to specific Figure and Axes instances, eliminating bugs caused by pyplot's implicit tracking of the 'current' active figure."
    },
    {
        "id": 281,
        "topic": "Day 01: Global Interpreter Lock (GIL) Concept",
        "question": "What is Python's Global Interpreter Lock (GIL) in standard CPython?",
        "code": None,
        "options": [
            "A) A lock that prevents files from being modified by two programs",
            "B) A mutex that prevents multiple native OS threads from executing Python bytecodes simultaneously in a single process",
            "C) A security lock preventing unauthorized Python module imports",
            "D) A hardware lock on the CPU core"
        ],
        "answer": "B",
        "explanation": "CPython's GIL is a mutex designed to make thread-unsafe reference counting memory management safe, restricting pure Python CPU-bound execution to one thread at a time per process."
    },
    {
        "id": 282,
        "topic": "Day 02: String intern() Explicit Invocation",
        "question": "What is the output of sys.intern('hello ' + 'world') is sys.intern('hello world')?",
        "code": 'import sys\ns1 = sys.intern("hello " + "world")\ns2 = sys.intern("hello world")\nprint(s1 is s2)',
        "options": [
            "A) True",
            "B) False",
            "C) TypeError",
            "D) None"
        ],
        "answer": "A",
        "explanation": "sys.intern() registers the string in CPython's internal string table and returns the canonical interned object reference. Since both strings have identical content, both calls return the same object (s1 is s2 is True)."
    },
    {
        "id": 283,
        "topic": "Day 03: Bisect Module for Sorted Sequences",
        "question": "What does bisect.bisect_left([10, 20, 30, 40], 25) return?",
        "code": 'import bisect\nidx = bisect.bisect_left([10, 20, 30, 40], 25)\nprint(idx)',
        "options": [
            "A) 1",
            "B) 2",
            "C) 3",
            "D) -1"
        ],
        "answer": "B",
        "explanation": "bisect_left uses binary search (O(log n)) to locate the insertion point that maintains sorted order. 25 belongs between 20 (index 1) and 30 (index 2), returning index 2."
    },
    {
        "id": 284,
        "topic": "Day 04: Dict Compact Layout in Python 3.6+",
        "question": "How did Raymond Hettinger's compact dict implementation in Python 3.6+ reduce dictionary memory consumption by 20-25% while guaranteeing insertion order?",
        "code": None,
        "options": [
            "A) By compressing keys using gzip in RAM",
            "B) By splitting the hash table into a sparse index array of byte indices and a compact dense entries array of (hash, key, value)",
            "C) By converting keys to integers",
            "D) By using binary search trees instead of hash tables"
        ],
        "answer": "B",
        "explanation": "The compact dict stores actual (hash, key, value) tuples consecutively in a dense array (which naturally preserves insertion order) and uses a small sparse hash index table containing integer offsets into the dense array."
    },
    {
        "id": 285,
        "topic": "Day 05: Function __closure__ Attribute",
        "question": "Where does Python store free variables referenced by a closure function?",
        "code": 'def make_adder(x):\n    def adder(y):\n        return x + y\n    return adder\na = make_adder(10)',
        "options": [
            "A) In a global dictionary",
            "B) In a tuple of cell objects accessible via adder.__closure__",
            "C) On the operating system stack",
            "D) In sys.modules"
        ],
        "answer": "B",
        "explanation": "Free variables captured by a closure are stored in cell objects inside the function's __closure__ attribute (a.__closure__[0].cell_contents is 10)."
    },
    {
        "id": 286,
        "topic": "Day 06: Method Type Binding (Bound Method)",
        "question": "What is the difference between Person.greet and p.greet where p = Person()?",
        "code": 'class Person:\n    def greet(self): pass\np = Person()',
        "options": [
            "A) Both are identical functions",
            "B) Person.greet is a function; p.greet is a bound method that automatically curries 'p' as the first argument 'self'",
            "C) p.greet cannot be passed as a callback",
            "D) Person.greet raises a TypeError when defined"
        ],
        "answer": "B",
        "explanation": "When accessed on a class, it is a plain function object. When accessed on an instance, the descriptor protocol (__get__) binds the instance to produce a 'method' object that automatically passes p to self."
    },
    {
        "id": 287,
        "topic": "Day 06: Class Creation via type()",
        "question": "How do you dynamically create a class named 'User' with attribute role='admin' using the type() metaclass constructor directly?",
        "code": None,
        "options": [
            "A) User = type('User', (), {'role': 'admin'})",
            "B) User = type.create('User', {'role': 'admin'})",
            "C) User = class('User', (), role='admin')",
            "D) User = type('User', role='admin')"
        ],
        "answer": "A",
        "explanation": "The 3-argument signature of type is: type(name, bases_tuple, dict_of_attributes). Thus, type('User', (), {'role': 'admin'}) dynamically constructs the class."
    },
    {
        "id": 288,
        "topic": "Day 07: SQLite Foreign Key Constraints Enforcement",
        "question": "Why does SQLite by default allow inserting rows that violate FOREIGN KEY constraints, and how is enforcement enabled?",
        "code": None,
        "options": [
            "A) Foreign keys are not supported in SQLite",
            "B) For historical backward-compatibility, foreign key enforcement is disabled by default; it must be enabled per-connection via 'PRAGMA foreign_keys = ON;'",
            "C) Foreign keys are only checked during commit()",
            "D) Python's DB-API disables foreign keys"
        ],
        "answer": "B",
        "explanation": "In SQLite, foreign key enforcement is disabled by default for backward compatibility. Executing cursor.execute('PRAGMA foreign_keys = ON;') is required to enforce them."
    },
    {
        "id": 289,
        "topic": "Day 08: Coroutine Delegation Protocol",
        "question": "What is the key difference between a Python generator and an async coroutine defined with 'async def'?",
        "code": None,
        "options": [
            "A) Generators produce streams of data via yield; async coroutines model asynchronous cooperative tasks managed by an event loop via await",
            "B) Async def cannot use loops",
            "C) Generators run in separate OS threads",
            "D) They are completely identical in implementation"
        ],
        "answer": "A",
        "explanation": "Generators are lazy data producers evaluated with next(). 'async def' coroutines are concurrency constructs integrated with an event loop (asyncio) that pause execution at 'await' points until futures resolve."
    },
    {
        "id": 290,
        "topic": "Day 09: WSGI Specification Architecture",
        "question": "What is the standard function signature of a WSGI-compliant application callable according to PEP 3333?",
        "code": None,
        "options": [
            "A) application(request, response)",
            "B) application(environ, start_response)",
            "C) application(http_stream)",
            "D) application(url, headers, body)"
        ],
        "answer": "B",
        "explanation": "WSGI (Web Server Gateway Interface) specifies that an application must be a callable accepting two parameters: environ (a dictionary of CGI environment variables) and start_response (a callback function taking status and headers)."
    },
    {
        "id": 291,
        "topic": "Day 10: NumPy Vectorization vs CPython Loop",
        "question": "Why is np.sum(large_array) orders of magnitude faster than Python's built-in sum(large_array)?",
        "code": None,
        "options": [
            "A) NumPy operates on contiguous blocks of homogenous C data types without type-checking or pointer chasing per element",
            "B) NumPy disables GIL and runs on GPU by default",
            "C) Built-in sum() uses recursion",
            "D) Python's sum() has a memory leak"
        ],
        "answer": "A",
        "explanation": "NumPy arrays store raw primitive types in contiguous memory buffers. Operations are compiled C loops with SIMD vectorization. Standard Python lists store pointers to heap-allocated PyObject wrappers, causing heavy cache misses and dynamic type checking."
    },
    {
        "id": 292,
        "topic": "Day 11: Pandas merge() Types",
        "question": "What is the output of pd.merge(df1, df2, on='id', how='left') when an id in df1 has no match in df2?",
        "code": None,
        "options": [
            "A) The row is dropped",
            "B) The row is retained, and columns from df2 are filled with NaN",
            "C) A KeyError is raised",
            "D) Columns from df2 are filled with empty strings ''"
        ],
        "answer": "B",
        "explanation": "A left outer join retains all rows from the left DataFrame. If there is no matching key in the right DataFrame, right-table columns are populated with NaN (null)."
    },
    {
        "id": 293,
        "topic": "Day 11: Pandas Indexing with .query()",
        "question": "What is the advantage of using df.query('Price > 20 and Units < 5') over standard bracket indexing?",
        "code": None,
        "options": [
            "A) It allows using natural logical operators ('and', 'or') without requiring bitwise operators ('&', '|') or parentheses",
            "B) It runs faster on very large DataFrames by evaluating expressions with NumExpr",
            "C) It provides a cleaner and more readable syntax",
            "D) All of the above"
        ],
        "answer": "D",
        "explanation": "df.query() evaluates string expressions using NumExpr (improving speed on large datasets) and accepts standard boolean keywords 'and'/'or' without parentheses."
    },
    {
        "id": 294,
        "topic": "Day 10: NumPy newaxis Dimension Expansion",
        "question": "What is the shape of arr[:, np.newaxis] where arr = np.array([1, 2, 3, 4])?",
        "code": 'arr = np.array([1, 2, 3, 4])\nexpanded = arr[:, np.newaxis]\nprint(expanded.shape)',
        "options": [
            "A) (4,)",
            "B) (4, 1)",
            "C) (1, 4)",
            "D) (4, 4)"
        ],
        "answer": "B",
        "explanation": "np.newaxis (an alias for None) inserts a new axis of length 1 at the specified dimension, transforming a 1D array of shape (4,) into a 2D column vector of shape (4, 1)."
    },
    {
        "id": 295,
        "topic": "Day 05: Argument Packing and Keyword Ordering",
        "question": "Which of the following function signatures is syntactically legal in Python 3?",
        "code": None,
        "options": [
            "A) def fn(a, *b, c=1, **d): pass",
            "B) def fn(**d, *b, a): pass",
            "C) def fn(*b, a, **d, e): pass",
            "D) def fn(a=1, b, **c): pass"
        ],
        "answer": "A",
        "explanation": "Valid parameter order is: positional-only (optional) -> standard positional -> var-positional (*args) -> keyword-only (c=1) -> var-keyword (**kwargs). Option A matches this order."
    },
    {
        "id": 296,
        "topic": "Day 06: Method Overriding and super() Delegation",
        "question": "What is the output of the following inheritance snippet?",
        "code": 'class Base:\n    def __init__(self):\n        self.val = 1\nclass Derived(Base):\n    def __init__(self):\n        self.val = 2\n        super().__init__()\nd = Derived()\nprint(d.val)',
        "options": [
            "A) 2",
            "B) 1",
            "C) 3",
            "D) None"
        ],
        "answer": "B",
        "explanation": "Derived sets self.val = 2, and then calls super().__init__(), which overwrites self.val to 1. Output is 1."
    },
    {
        "id": 297,
        "topic": "Day 07: Text vs Binary Mode Cursor Offsets",
        "question": "In Python 3 text mode ('r'), why does f.seek(offset, 1) or f.seek(offset, 2) raise an io.UnsupportedOperation when offset is non-zero?",
        "code": None,
        "options": [
            "A) Multi-byte Unicode encodings (like UTF-8) mean character offsets do not match byte offsets, making arbitrary relative byte seeking invalid in text streams",
            "B) Operating systems prohibit seek in text files",
            "C) Python text files do not have file descriptors",
            "D) Seek is only available in write mode"
        ],
        "answer": "A",
        "explanation": "In text mode, character-to-byte mapping varies (e.g. variable-length UTF-8 encodings). Python forbids relative seeking with non-zero offsets in text mode to avoid landing in the middle of a multi-byte character."
    },
    {
        "id": 298,
        "topic": "Day 10: BeautifulSoup find vs select",
        "question": "What is the output of soup.find('div', id='main') vs soup.select_one('#main')?",
        "code": None,
        "options": [
            "A) Both locate and return the first matching Tag element with id='main' (or None if not found)",
            "B) find returns a list; select_one returns a string",
            "C) select_one is only for classes",
            "D) find raises an error if id is missing"
        ],
        "answer": "A",
        "explanation": "Both find(..., id='main') and select_one('#main') return the first matching Tag element, or None if no match is found."
    },
    {
        "id": 299,
        "topic": "Day 11: Pandas pivot_table() Aggregation",
        "question": "What is the primary difference between df.pivot() and df.pivot_table() in Pandas?",
        "code": None,
        "options": [
            "A) df.pivot() requires unique index/column combinations (raises ValueError on duplicates); df.pivot_table() aggregates duplicate combinations using aggfunc (default mean)",
            "B) df.pivot_table() is deprecated",
            "C) df.pivot() only works on numbers",
            "D) Both do not support aggregation"
        ],
        "answer": "A",
        "explanation": "df.pivot() reshapes data without aggregation and raises an error on duplicate index/columns. df.pivot_table() performs aggregation (default: np.mean) across duplicate entries."
    },
    {
        "id": 300,
        "topic": "Day 11: Matplotlib plt.subplots figsize Units",
        "question": "In Matplotlib, what unit of measurement is used for figsize=(width, height) in plt.subplots(figsize=(10, 6))?",
        "code": 'fig, ax = plt.subplots(figsize=(10, 6))',
        "options": [
            "A) Centimeters",
            "B) Pixels",
            "C) Inches",
            "D) Millimeters"
        ],
        "answer": "C",
        "explanation": "Matplotlib figures are measured in inches: figsize=(width_in_inches, height_in_inches). Combined with dpi (dots per inch), it determines the final pixel resolution."
    }
]

with open(r"d:\Engineering\CDAC_ALL_MODULES\Python\questions_advanced.py", "w", encoding="utf-8") as f:
    f.write('"""Advanced Question Bank (Q201 - Q300)"""\n\n')
    f.write("ADVANCED_QUESTIONS = " + json.dumps(questions, indent=4))
print(f"Successfully generated {len(questions)} advanced questions.")
