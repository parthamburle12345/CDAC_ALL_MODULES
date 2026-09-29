# 🐍 Python MCQ Test Bank — CDAC PGCP-AI
## Complete Preparation Guide: Day 1 → Day 11
### 150 Questions | Easy (50) · Medium (50) · Hard (50) | With Code Snippets & Explanations

---

> **How to Use This File**
> - Answer each question **on paper** before reading the explanation.
> - The correct answer is marked with ✅.
> - Each question includes a **📝 Explanation** to reinforce understanding.
> - **Difficulty Map**: Easy → Day 1–4 basics | Medium → Day 4–7 | Hard → Day 7–11 advanced topics.

---

# 🟢 SECTION 1: EASY (Questions 1–50)
> *Topics: Python History, Basic Syntax, Data Types, Variables, Operators, I/O, Conditionals, Loops, Strings, Tuples, Lists, Dictionaries*

---

## Q1. Who created the Python programming language?
- A) James Gosling
- B) Dennis Ritchie  
- C) ✅ **Guido van Rossum**
- D) Bjarne Stroustrup

📝 **Explanation:** Python was created by **Guido van Rossum** in the late 1980s and first released in 1991. He named it after the British comedy group **Monty Python**, not the snake!

---

## Q2. What does the following code print?
```python
print("Hello", "World", sep="-")
```
- A) Hello World
- B) Hello, World
- C) ✅ **Hello-World**
- D) HelloWorld

📝 **Explanation:** The `sep` parameter in `print()` defines what goes **between** multiple items. Here `sep="-"` means items are joined by a hyphen. Output: `Hello-World`

---

## Q3. What is the output of `10 // 3`?
- A) 3.33
- B) ✅ **3**
- C) 1
- D) 4

📝 **Explanation:** `//` is **floor division** — it divides and discards the decimal part, returning an integer. `10 // 3 = 3` (not 3.33). Compare: `10 / 3 = 3.333...`

---

## Q4. Which of the following is a valid Python variable name?
- A) `2nd_value`
- B) `my-value`
- C) ✅ **`my_value`**
- D) `my value`

📝 **Explanation:** Variable names cannot start with a digit, cannot contain hyphens or spaces. Only letters, digits (not first), and underscores are allowed.

---

## Q5. What does `input()` always return?
- A) An integer
- B) A float
- C) ✅ **A string**
- D) Whatever type the user enters

📝 **Explanation:** This is a critical Python rule! `input()` **always returns a string (str)**, regardless of what the user types. If you need a number, you must cast: `int(input())` or `float(input())`.

---

## Q6. What is the output of this code?
```python
x = 5
x += 3
print(x)
```
- A) 5
- B) 3
- C) ✅ **8**
- D) `5 + 3`

📝 **Explanation:** `x += 3` is shorthand for `x = x + 3`. So `5 + 3 = 8`. The variable `x` is updated in-place.

---

## Q7. Which keyword is used to define a function in Python?
- A) `function`
- B) `func`
- C) ✅ **`def`**
- D) `define`

📝 **Explanation:** Python uses the `def` keyword to define functions. Syntax: `def function_name(parameters):`. Unlike C/Java, there are no curly braces — indentation marks the function body.

---

## Q8. What is the output of this code?
```python
for i in range(3):
    print(i)
```
- A) 1 2 3
- B) ✅ **0 1 2**
- C) 0 1 2 3
- D) 1 2

📝 **Explanation:** `range(3)` generates numbers from **0 to 2** (stop is exclusive). So it prints `0`, `1`, `2` on separate lines. Remember: `range(n)` always starts at 0.

---

## Q9. Which data type is immutable in Python?
- A) List
- B) Dictionary
- C) ✅ **Tuple**
- D) Set

📝 **Explanation:** A **Tuple** is immutable — once created, its elements cannot be changed. Lists, dictionaries, and sets are all mutable (can be changed after creation).

---

## Q10. What is the output?
```python
x = "Python"
print(x[0])
```
- A) y
- B) ✅ **P**
- C) `IndexError`
- D) `n`

📝 **Explanation:** Python uses **zero-based indexing**. Index `[0]` refers to the **first** character. For `"Python"`, index 0 is `'P'`.

---

## Q11. What is the result of `5 % 2`?
- A) 2
- B) 2.5
- C) ✅ **1**
- D) 0

📝 **Explanation:** `%` is the **modulo operator** — it returns the **remainder** of division. `5 ÷ 2 = 2 remainder 1`. So `5 % 2 = 1`.

---

## Q12. What is the correct way to write a single-line comment in Python?
- A) `// This is a comment`
- B) `/* This is a comment */`
- C) ✅ **`# This is a comment`**
- D) `-- This is a comment`

📝 **Explanation:** Python uses the `#` symbol for single-line comments. Everything after `#` on the same line is ignored by the interpreter.

---

## Q13. What does `len("Hello")` return?
- A) 4
- B) ✅ **5**
- C) 6
- D) `TypeError`

📝 **Explanation:** `len()` returns the **number of characters** in a string. `"Hello"` has 5 characters: H-e-l-l-o. So `len("Hello") = 5`.

---

## Q14. What is the output?
```python
name = "alice"
print(name.upper())
```
- A) alice
- B) Alice
- C) ✅ **ALICE**
- D) `error`

📝 **Explanation:** `.upper()` converts **all characters to uppercase**. `"alice".upper()` → `"ALICE"`. Note: The original string is unchanged (strings are immutable).

---

## Q15. Which of these creates a tuple with one element?
- A) `t = (1)`
- B) `t = [1]`
- C) ✅ **`t = (1,)`**
- D) `t = {1}`

📝 **Explanation:** Without the trailing comma, `(1)` is just a parenthesized integer (not a tuple). The **trailing comma** is mandatory for single-element tuples: `(1,)`. `[1]` is a list, `{1}` is a set.

---

## Q16. What is the output?
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```
- A) `[1, 2, 3]`
- B) `[4, 1, 2, 3]`
- C) ✅ **`[1, 2, 3, 4]`**
- D) `TypeError`

📝 **Explanation:** `.append()` adds an element **at the end** of the list. After `append(4)`, the list becomes `[1, 2, 3, 4]`.

---

## Q17. How do you access the value for key `"name"` in a dictionary?
```python
d = {"name": "Alice", "age": 25}
```
- A) `d.name`
- B) `d[0]`
- C) ✅ **`d["name"]`**
- D) `d.get_value("name")`

📝 **Explanation:** Dictionary values are accessed using **square brackets with the key**: `d["name"]` returns `"Alice"`. You can also use `d.get("name")` which returns `None` if the key doesn't exist.

---

## Q18. What is the output?
```python
print(type(3.14))
```
- A) `<class 'int'>`
- B) ✅ **`<class 'float'>`**
- C) `<class 'double'>`
- D) `<class 'number'>`

📝 **Explanation:** `3.14` is a **floating-point number**, so `type(3.14)` returns `<class 'float'>`. Python doesn't have a `double` type like Java/C++.

---

## Q19. What does this print?
```python
x = 10
if x > 5:
    print("Big")
else:
    print("Small")
```
- A) Small
- B) ✅ **Big**
- C) Big Small
- D) Nothing

📝 **Explanation:** `x = 10`, and `10 > 5` is `True`. So the `if` block executes and prints `"Big"`. The `else` block is skipped.

---

## Q20. What is the output?
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```
- A) 1 2 3 4 5
- B) 1 2 3
- C) ✅ **1 2**
- D) 3 4 5

📝 **Explanation:** The loop runs from 1 to 5. When `i == 3`, the `break` statement **immediately exits the loop**. So only `1` and `2` are printed before the break.

---

## Q21. What does this code output?
```python
print("ha" * 3)
```
- A) ha ha ha
- B) ha3
- C) ✅ **hahaha**
- D) `TypeError`

📝 **Explanation:** The `*` operator with a string **repeats** it. `"ha" * 3` = `"hahaha"`. No spaces are added — just the string repeated 3 times.

---

## Q22. What is the output?
```python
nums = [10, 20, 30, 40]
print(nums[-1])
```
- A) 10
- B) ✅ **40**
- C) `IndexError`
- D) -40

📝 **Explanation:** **Negative indexing** in Python counts from the end. `-1` refers to the **last element**. `nums[-1] = 40`. `-2` would be `30`, and so on.

---

## Q23. Which operator checks if two values are equal in Python?
- A) `=`
- B) ✅ **`==`**
- C) `===`
- D) `is`

📝 **Explanation:** `=` is the **assignment operator**. `==` is the **equality comparison operator** that returns `True` or `False`. `===` doesn't exist in Python. `is` checks **identity** (same memory object), not equality of values.

---

## Q24. What is the output?
```python
x = True
y = False
print(x and y)
```
- A) True
- B) ✅ **False**
- C) 1
- D) `TypeError`

📝 **Explanation:** `and` returns `True` only if **both** values are `True`. Since `y = False`, `True and False = False`.

---

## Q25. How do you convert the string `"42"` to an integer?
- A) `str("42")`
- B) ✅ **`int("42")`**
- C) `float("42")` returns integer
- D) `number("42")`

📝 **Explanation:** `int("42")` converts the string `"42"` to the integer `42`. `float("42")` would give `42.0`. `str()` converts TO a string. There is no `number()` built-in function.

---

## Q26. What is the output of this slice?
```python
s = "PYTHON"
print(s[1:4])
```
- A) PYT
- B) ✅ **YTH**
- C) YTHO
- D) Python

📝 **Explanation:** Slicing `[1:4]` extracts characters from index 1 (inclusive) to index 4 (exclusive). `P=0, Y=1, T=2, H=3, O=4, N=5`. So indices 1,2,3 = `Y`, `T`, `H` → `"YTH"`.

---

## Q27. What is the output?
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```
- A) apple
- B) ✅ **banana**
- C) cherry
- D) `IndexError`

📝 **Explanation:** Lists use zero-based indexing. Index `0` = `"apple"`, index `1` = `"banana"`, index `2` = `"cherry"`. So `fruits[1]` is `"banana"`.

---

## Q28. Which string method removes leading and trailing whitespace?
- A) `.trim()`
- B) `.clean()`
- C) ✅ **`.strip()`**
- D) `.remove()`

📝 **Explanation:** `.strip()` removes whitespace from **both ends** of a string. `.lstrip()` strips from the left only, `.rstrip()` from the right only. Python has no `.trim()` method (unlike JavaScript).

---

## Q29. What is the output?
```python
d = {"a": 1, "b": 2}
print(len(d))
```
- A) 1
- B) ✅ **2**
- C) 3
- D) `{"a": 1, "b": 2}`

📝 **Explanation:** `len()` on a dictionary returns the **number of key-value pairs**. Dictionary `d` has 2 pairs: `"a": 1` and `"b": 2`. So `len(d) = 2`.

---

## Q30. What does `not True` evaluate to?
- A) True
- B) ✅ **False**
- C) 0
- D) `None`

📝 **Explanation:** `not` is the logical negation operator. `not True = False`. `not False = True`. It reverses the boolean value.

---

## Q31. What is the output?
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
- A) 1 2 3
- B) ✅ **0 1 2**
- C) 0 1 2 3
- D) Infinite loop

📝 **Explanation:** The loop starts at `count = 0` and runs while `count < 3`. It prints 0, 1, 2, then `count` becomes 3, the condition `3 < 3` is `False`, and the loop ends.

---

## Q32. Which of the following is a FALSY value in Python?
- A) `"0"` (non-empty string)
- B) `[0]` (list with one element)
- C) ✅ **`[]` (empty list)**
- D) `(0,)` (non-empty tuple)

📝 **Explanation:** Falsy values: `None`, `False`, `0`, `0.0`, `""`, `[]`, `()`, `{}`. An **empty list `[]`** is falsy. `"0"` (non-empty string), `[0]`, and `(0,)` are all **truthy**.

---

## Q33. How do you add a key-value pair to an existing dictionary?
```python
d = {"name": "Bob"}
```
- A) `d.add("age", 25)`
- B) ✅ **`d["age"] = 25`**
- C) `d.insert("age", 25)`
- D) `d.append({"age": 25})`

📝 **Explanation:** To add or update a dictionary entry, simply use **assignment with square brackets**: `d["age"] = 25`. Dictionaries don't have `.add()`, `.insert()`, or `.append()` methods.

---

## Q34. What is the output?
```python
x = "hello world"
print(x.split())
```
- A) `"hello world"`
- B) ✅ **`['hello', 'world']`**
- C) `('hello', 'world')`
- D) `{'hello', 'world'}`

📝 **Explanation:** `.split()` without arguments splits on **whitespace** by default and returns a **list**. `"hello world".split()` = `['hello', 'world']`.

---

## Q35. What is the output?
```python
t = (1, 2, 3)
print(t[1])
```
- A) 1
- B) ✅ **2**
- C) 3
- D) `(2,)`

📝 **Explanation:** Tuples support the same zero-based indexing as lists and strings. `t[1]` = the second element = `2`.

---

## Q36. What does the `pass` statement do in Python?
- A) Exits the function
- B) Skips to the next iteration
- C) Terminates the loop
- D) ✅ **Does nothing — it is a syntactic placeholder**

📝 **Explanation:** `pass` is a **null operation** — it does absolutely nothing when executed. It's used as a placeholder where Python syntax requires a code block but you don't want to execute any code yet.

---

## Q37. What is the output?
```python
print(2 ** 10)
```
- A) 20
- B) ✅ **1024**
- C) 512
- D) 2048

📝 **Explanation:** `**` is the **exponentiation operator**. `2 ** 10 = 2^10 = 1024`.

---

## Q38. Which method checks if a string starts with a specific prefix?
- A) `.begins_with()`
- B) `.has_prefix()`
- C) ✅ **`.startswith()`**
- D) `.starts()`

📝 **Explanation:** `.startswith(prefix)` returns `True` if the string begins with the given prefix. Similarly, `.endswith(suffix)` checks the end. Example: `"Hello".startswith("He")` → `True`.

---

## Q39. What is the output?
```python
nums = [3, 1, 4, 1, 5, 9]
nums.sort()
print(nums)
```
- A) `[3, 1, 4, 1, 5, 9]`
- B) ✅ **`[1, 1, 3, 4, 5, 9]`**
- C) `[9, 5, 4, 3, 1, 1]`
- D) `TypeError`

📝 **Explanation:** `.sort()` sorts the list **in-place** in ascending order by default. The original list is modified. Result: `[1, 1, 3, 4, 5, 9]`. Use `nums.sort(reverse=True)` for descending.

---

## Q40. What is `type(None)`?
- A) `<class 'bool'>`
- B) `<class 'void'>`
- C) ✅ **`<class 'NoneType'>`**
- D) `<class 'null'>`

📝 **Explanation:** `None` is a special singleton constant representing the **absence of a value**. Its type is `NoneType`. It's Python's equivalent of `null` in other languages.

---

## Q41. What does the `continue` statement do inside a loop?
- A) Exits the loop completely
- B) Pauses the loop
- C) ✅ **Skips the rest of the current iteration and moves to the next**
- D) Does nothing

📝 **Explanation:** `continue` **skips all remaining code in the current iteration** and jumps directly to the next cycle of the loop. Compare with `break` which exits the loop entirely.

---

## Q42. What is the output?
```python
text = "banana"
print(text.count("a"))
```
- A) 1
- B) 2
- C) ✅ **3**
- D) `None`

📝 **Explanation:** `.count(sub)` counts **non-overlapping occurrences** of a substring. In `"banana"`: b-**a**-n-**a**-n-**a** — the letter `"a"` appears **3 times**.

---

## Q43. Which data type stores a collection of UNIQUE items only?
- A) `list`
- B) `tuple`
- C) `dict`
- D) ✅ **`set`**

📝 **Explanation:** A **set** automatically enforces uniqueness — duplicate values are automatically removed. `{1, 2, 2, 3}` → `{1, 2, 3}`. Sets are unordered and mutable.

---

## Q44. What is the output?
```python
a, b, c = 10, 20, 30
print(b)
```
- A) 10
- B) ✅ **20**
- C) 30
- D) `10, 20, 30`

📝 **Explanation:** This is **tuple unpacking** (multiple assignment). `a = 10`, `b = 20`, `c = 30` all happen in one line. `print(b)` outputs `20`.

---

## Q45. What does `x = y = z = 0` do?
- A) Causes a syntax error
- B) Only assigns `z = 0`
- C) ✅ **Assigns 0 to all three variables**
- D) Creates a tuple

📝 **Explanation:** Python allows **chained assignment**. `x = y = z = 0` evaluates `0` first, then assigns it to `z`, then `y`, then `x`. All three variables now point to the integer object `0`.

---

## Q46. What is the output?
```python
print("  hello  ".strip())
```
- A) `"  hello  "`
- B) ✅ **`hello`**
- C) `hello  `
- D) `  hello`

📝 **Explanation:** `.strip()` removes **leading and trailing whitespace**. `"  hello  ".strip()` → `"hello"` (no surrounding spaces).

---

## Q47. What is the output?
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[::2])
```
- A) `[2, 4]`
- B) ✅ **`[1, 3, 5]`**
- C) `[1, 2, 3]`
- D) `[5, 4, 3, 2, 1]`

📝 **Explanation:** `[::2]` is slicing with a **step of 2**. Start at index 0, take every 2nd element: index 0→1, index 2→3, index 4→5. Result: `[1, 3, 5]`.

---

## Q48. Which built-in function returns the number of items in a list?
- A) `size()`
- B) `count()`
- C) ✅ **`len()`**
- D) `length()`

📝 **Explanation:** `len()` is the built-in function that returns the number of items in a sequence. Python has no `size()` or `length()` built-in functions.

---

## Q49. What is the output?
```python
d = {"x": 10, "y": 20, "z": 30}
del d["y"]
print(len(d))
```
- A) 3
- B) ✅ **2**
- C) 1
- D) `KeyError`

📝 **Explanation:** `del d["y"]` **removes the key-value pair** `"y": 20` from the dictionary. After deletion, the dictionary has 2 entries. So `len(d) = 2`.

---

## Q50. What is the output?
```python
s = "Python"
print(s[-3:])
```
- A) `Pyt`
- B) ✅ **`hon`**
- C) `thon`
- D) `IndexError`

📝 **Explanation:** `s[-3:]` slices from the **3rd character from the end** to the end. `P=-6, y=-5, t=-4, h=-3, o=-2, n=-1`. From index `-3` to end: `h`, `o`, `n` = `"hon"`.

---

---

# 🟡 SECTION 2: MEDIUM (Questions 51–100)
> *Topics: Exception Handling, Functions, Lambda, Scopes, OOP, Comprehensions, RegEx, File I/O, JSON, CSV, Pickle, SQLite, Decorators*

---

## Q51. What does this code print?
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```
- A) `Cannot divide by zero` only
- B) `Done` only
- C) ✅ **`Cannot divide by zero` then `Done`**
- D) `ZeroDivisionError` traceback

📝 **Explanation:** When `10 / 0` raises `ZeroDivisionError`, the `except` block catches it. The `finally` block **always runs**, regardless of exception. Both lines are printed.

---

## Q52. What is the LEGB rule in Python?
- A) List, Enum, Global, Boolean
- B) ✅ **Local, Enclosing, Global, Built-in**
- C) Lambda, Expression, Generator, Block
- D) Loop, Exception, Group, Break

📝 **Explanation:** The **LEGB rule** is Python's variable lookup order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in. Python searches in this exact sequence when resolving variable names.

---

## Q53. What is the output?
```python
add = lambda x, y: x + y
print(add(3, 7))
```
- A) `lambda x, y: x + y`
- B) `<function <lambda>>`
- C) ✅ **10**
- D) `TypeError`

📝 **Explanation:** A **lambda function** is a compact anonymous function. `lambda x, y: x + y` takes two arguments and returns their sum. `add(3, 7)` calls it with `3` and `7`, returning `10`.

---

## Q54. What does this list comprehension produce?
```python
result = [x**2 for x in range(1, 6)]
print(result)
```
- A) `[1, 2, 3, 4, 5]`
- B) ✅ **`[1, 4, 9, 16, 25]`**
- C) `[1, 4, 9, 16, 25, 36]`
- D) `[2, 4, 6, 8, 10]`

📝 **Explanation:** List comprehension `[x**2 for x in range(1, 6)]` squares each number from 1 to 5: `1²=1, 2²=4, 3²=9, 4²=16, 5²=25`. Result: `[1, 4, 9, 16, 25]`.

---

## Q55. What does `*args` collect in a function?
```python
def my_func(*args):
    print(type(args))

my_func(1, 2, 3)
```
- A) `<class 'list'>`
- B) ✅ **`<class 'tuple'>`**
- C) `<class 'dict'>`
- D) Three separate variables

📝 **Explanation:** `*args` collects all **extra positional arguments** into a **tuple** (not a list!). `type(args)` prints `<class 'tuple'>`. `**kwargs` collects keyword arguments as a dictionary.

---

## Q56. What is the output?
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()
```
- A) 10
- B) ✅ **20**
- C) `NameError`
- D) `UnboundLocalError`

📝 **Explanation:** The `nonlocal` keyword allows the inner function to **modify a variable in the enclosing (outer) function's scope**. Without `nonlocal`, a new local `x` would be created. With it, the outer `x` is changed to `20`.

---

## Q57. What exception is raised when you access a dictionary key that doesn't exist?
```python
d = {"a": 1}
print(d["b"])
```
- A) `IndexError`
- B) ✅ **`KeyError`**
- C) `ValueError`
- D) `AttributeError`

📝 **Explanation:** When you access a key that doesn't exist using `[]`, Python raises a **`KeyError`**. Use `d.get("b")` to safely return `None` instead, or `d.get("b", default)` for a custom default.

---

## Q58. What does `@staticmethod` do?
- A) Makes a method only callable on the class, not instances
- B) ✅ **Makes a method that doesn't receive `self` or `cls`**
- C) Makes a method that cannot be overridden
- D) Converts a method to a class attribute

📝 **Explanation:** A `@staticmethod` belongs to the class namespace but **doesn't receive `self` (instance) or `cls` (class)** as the first argument. It behaves like a regular function organized within a class for logical grouping.

---

## Q59. What is the output?
```python
class Animal:
    def sound(self):
        return "Generic Sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

d = Dog()
print(d.sound())
```
- A) `Generic Sound`
- B) ✅ **`Woof`**
- C) `Generic Sound Woof`
- D) `AttributeError`

📝 **Explanation:** This demonstrates **method overriding** (polymorphism). The `Dog` class defines its own `sound()` that **overrides** the parent class's version. When called on a `Dog` instance, Python uses the child class's method.

---

## Q60. What does this code do?
```python
with open("file.txt", "w") as f:
    f.write("Hello")
```
- A) Reads the file
- B) ✅ **Creates/overwrites the file and writes "Hello"**
- C) Appends "Hello" to the file
- D) Raises `FileNotFoundError`

📝 **Explanation:** Mode `"w"` **creates the file if it doesn't exist**, or **truncates (erases) it if it does**, then writes. The `with` statement ensures the file is **automatically closed** when the block ends.

---

## Q61. What is the output?
```python
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evens)
```
- A) `[1, 3, 5]`
- B) ✅ **`[2, 4, 6]`**
- C) `[1, 2, 3, 4, 5, 6]`
- D) `True False True False True False`

📝 **Explanation:** `filter()` keeps elements where the function returns `True`. `x % 2 == 0` is True for even numbers: 2, 4, 6. `list()` converts the filter object to a list.

---

## Q62. What does `json.dumps()` do?
- A) Reads a JSON file
- B) ✅ **Converts a Python object to a JSON-formatted string**
- C) Converts a JSON string to a Python object
- D) Saves a Python object to a JSON file

📝 **Explanation:** Think: **`dumps` = dump to String**. `json.dumps(obj)` serializes `obj` into a JSON string. `json.loads(s)` does the reverse. `json.dump(obj, f)` writes to a file stream.

---

## Q63. What is the output?
```python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)
```
- A) 0
- B) 1
- C) ✅ **2**
- D) `AttributeError`

📝 **Explanation:** `count = 0` is a **class variable** — shared by ALL instances. Each instantiation calls `__init__`, incrementing the shared counter. After creating `c1` and `c2`, `count = 2`.

---

## Q64. What does `__init__` do in a Python class?
- A) It is the class's `main()` function
- B) ✅ **It is the constructor/initializer called automatically when an object is created**
- C) It destroys the object when done
- D) It makes the class iterable

📝 **Explanation:** `__init__` is the **initializer (constructor)** method. It's automatically called when a new object is instantiated. It receives `self` (the new object) and sets up instance attributes.

---

## Q65. What will happen when you run this code?
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 99
```
- A) `my_tuple` becomes `(99, 2, 3)`
- B) ✅ **`TypeError: 'tuple' object does not support item assignment`**
- C) `AttributeError`
- D) The assignment is silently ignored

📝 **Explanation:** Tuples are **immutable** — their elements cannot be changed after creation. Attempting to assign raises a `TypeError`. To "modify" a tuple, you must create a new one.

---

## Q66. What is the output?
```python
import re
result = re.findall(r"\d+", "I have 3 cats and 12 dogs")
print(result)
```
- A) `[3, 12]` as integers
- B) ✅ **`['3', '12']` as strings**
- C) `None`
- D) `Match object`

📝 **Explanation:** `re.findall()` returns all non-overlapping matches as a **list of strings**. `\d+` matches one or more digits. The matches `"3"` and `"12"` are returned as strings, not integers.

---

## Q67. What does `@classmethod` receive as its first parameter?
- A) `self` — the current instance
- B) ✅ **`cls` — the class itself**
- C) Nothing
- D) The module name

📝 **Explanation:** A `@classmethod` receives the **class itself** as its first argument, conventionally named `cls`. It can access and modify class-level state. Often used as **factory methods** (alternative constructors).

---

## Q68. What is the output?
```python
squares = {x: x**2 for x in range(1, 4)}
print(squares)
```
- A) `[1, 4, 9]`
- B) `{1, 4, 9}`
- C) ✅ **`{1: 1, 2: 4, 3: 9}`**
- D) `(1, 4, 9)`

📝 **Explanation:** This is a **dictionary comprehension** with syntax `{key: value for ...}`. For each `x` in 1, 2, 3: key is `x`, value is `x²`. Result: `{1: 1, 2: 4, 3: 9}`.

---

## Q69. What is Python name mangling?
```python
class Foo:
    def __init__(self):
        self.__secret = 42
```
- A) It deletes the attribute entirely
- B) ✅ **It renames `__secret` to `_Foo__secret` internally to prevent accidental access**
- C) It makes the attribute read-only
- D) It encrypts the attribute value

📝 **Explanation:** Python **name mangling** transforms `self.__secret` (double underscore prefix) into `self._Foo__secret` internally. This prevents accidental access from outside the class while still allowing access via `obj._Foo__secret`.

---

## Q70. What does this code output?
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
```
- A) `Hello, Alice!` and `Hello, Bob!`
- B) ✅ **`Hello, Alice!` and `Hi, Bob!`**
- C) `Alice, Hello!` and `Bob, Hi!`
- D) `SyntaxError`

📝 **Explanation:** `greeting="Hello"` is a **default parameter**. When called without `greeting`, it uses `"Hello"`. When provided explicitly (`"Hi"`), the default is overridden.

---

## Q71. What exception does this raise?
```python
int("hello")
```
- A) `TypeError`
- B) ✅ **`ValueError`**
- C) `AttributeError`
- D) `ConversionError`

📝 **Explanation:** `int("hello")` raises `ValueError: invalid literal for int()`. The type is correct (strings can be passed to `int()`), but the **value** `"hello"` cannot be converted. `TypeError` would occur with wrong types like `int([1, 2])`.

---

## Q72. What is the output?
```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))
```
- A) 9
- B) ✅ **24**
- C) `2 3 4`
- D) `TypeError`

📝 **Explanation:** `*args` collects positional arguments as a tuple: `(2, 3, 4)`. The loop multiplies them: `1 × 2 = 2`, `2 × 3 = 6`, `6 × 4 = 24`. Returns `24`.

---

## Q73. What is the difference between `re.match()` and `re.search()`?
- A) They are identical
- B) ✅ **`match()` checks only the beginning; `search()` scans the whole string**
- C) `search()` checks only the beginning; `match()` scans the whole string
- D) `match()` returns all matches; `search()` returns the first

📝 **Explanation:** `re.match(pattern, string)` only tries to match at the **beginning of the string**. `re.search(pattern, string)` scans through the **entire string** and returns the first match anywhere.

---

## Q74. What is the purpose of `try-finally`?
- A) The `finally` block runs only if no exception occurred
- B) The `finally` block runs only if an exception occurred
- C) ✅ **The `finally` block ALWAYS runs, exception or not**
- D) `finally` is optional and rarely used

📝 **Explanation:** The `finally` block is **guaranteed to execute** regardless of whether an exception was raised. This makes it perfect for cleanup: closing files, releasing database connections, freeing resources.

---

## Q75. What is the output?
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Vehicle: {self.brand}"

v = Vehicle("Toyota")
print(v)
```
- A) `<__main__.Vehicle object at 0x...>`
- B) ✅ **`Vehicle: Toyota`**
- C) `Vehicle`
- D) `Toyota`

📝 **Explanation:** `__str__` is the **string representation** dunder method. When you `print()` an object, Python calls `__str__`. Without it, you'd get the default memory address format.

---

## Q76. Which mode opens a file for APPENDING (not overwriting)?
- A) `"w"`
- B) `"r"`
- C) ✅ **`"a"`**
- D) `"x"`

📝 **Explanation:** File modes: `"r"` = read, `"w"` = write (truncates existing), `"a"` = **append** (keeps existing content, adds at end), `"x"` = exclusive creation (fails if file exists).

---

## Q77. What is the output?
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
```
- A) `[1, 2, 3, 4, 5]`
- B) ✅ **`[1, 4, 9, 16, 25]`**
- C) `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`
- D) `<map object>`

📝 **Explanation:** `map()` applies the function to **every element** of the iterable. The lambda squares each number. `list()` converts the map object to a list: `[1, 4, 9, 16, 25]`.

---

## Q78. What does `super().__init__()` do in a child class?
- A) Creates a new instance of the parent class
- B) ✅ **Calls the parent class's `__init__` method**
- C) Deletes the parent class
- D) Returns the parent class object

📝 **Explanation:** `super()` returns a proxy object that delegates method calls to the parent class. `super().__init__()` explicitly calls the **parent's initializer** so inherited attributes are properly set up.

---

## Q79. What is output by this code?
```python
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(type(json_str))
```
- A) `<class 'dict'>`
- B) ✅ **`<class 'str'>`**
- C) `<class 'bytes'>`
- D) `<class 'json'>`

📝 **Explanation:** `json.dumps()` converts a Python dict to a **JSON string** (`str`). The result is always a string type. Use `json.loads(json_str)` to parse it back to a Python dict.

---

## Q80. What does `cursor.fetchall()` return in SQLite?
- A) A single row as a tuple
- B) ✅ **A list of all remaining rows**
- C) A generator object
- D) A dictionary of column names and values

📝 **Explanation:** `fetchall()` retrieves **all remaining rows** from the result set as a list of tuples (or `sqlite3.Row` objects if `row_factory` is set). `fetchone()` gets one row, `fetchmany(n)` gets up to n rows.

---

## Q81. What happens when you try to pickle a lambda function?
- A) It works fine
- B) The lambda is converted to a regular function
- C) ✅ **`PicklingError` — lambda functions cannot be pickled**
- D) The lambda's code is stored as a string

📝 **Explanation:** **Lambda functions cannot be pickled** because they are anonymous and have no module-level name to reference. Top-level named functions can be pickled by name. This is a key limitation of pickle vs. JSON.

---

## Q82. What is the output?
```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Alice")
print(p1 == p2)
```
- A) ✅ **`False`**
- B) `True`
- C) `TypeError`
- D) Depends on Python version

📝 **Explanation:** By default, `==` on custom objects checks **identity** (same memory address), not equality of attributes. `p1` and `p2` are two different objects in memory, so `p1 == p2` is `False`. Define `__eq__` to change this behavior.

---

## Q83. What does `enumerate()` do?
```python
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)
```
- A) Returns pairs of (value, index)
- B) ✅ **Returns pairs of (index, value)**
- C) Returns only the indices
- D) Sorts the list first, then returns it

📝 **Explanation:** `enumerate(iterable)` returns an iterator of `(index, value)` tuples. Output: `0 a`, `1 b`, `2 c`. You can start from a different index: `enumerate(list, start=1)`.

---

## Q84. Which is the CORRECT way to prevent SQL injection in `sqlite3`?
- A) `f"SELECT * FROM users WHERE name = '{user_input}'"`
- B) ✅ **`cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))`**
- C) `cursor.execute("SELECT * FROM users WHERE name = " + user_input)`
- D) Sanitize the string manually before concatenating

📝 **Explanation:** Always use **parameterized queries** with `?` placeholders. The `sqlite3` driver safely escapes the parameters, preventing SQL injection attacks. String formatting/concatenation allows malicious payloads like `' OR '1'='1`.

---

## Q85. What is the output?
```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
```
- A) 0, 0
- B) 1, 1
- C) ✅ **1 then 2**
- D) `NameError`

📝 **Explanation:** This is a **closure** — `increment` remembers the `count` variable from `counter`'s scope. Each call to `c()` increments and returns the persisted `count`. First call: `1`, second call: `2`.

---

## Q86. What does `@property` allow you to do?
- A) Make a class variable accessible from outside
- B) ✅ **Access a method as if it were an attribute (without parentheses)**
- C) Make an attribute permanently read-only
- D) Define multiple versions of the same method

📝 **Explanation:** `@property` transforms a method into a **getter property**. You call `obj.balance` (no parentheses) instead of `obj.balance()`. Combined with `@balance.setter`, you can add validation to attribute assignment.

---

## Q87. What is the output?
```python
import re
text = "Hello, World!"
pattern = r"W\w+"
match = re.search(pattern, text)
print(match.group())
```
- A) `Hello`
- B) ✅ **`World`**
- C) `World!`
- D) `None`

📝 **Explanation:** Pattern `W\w+` matches `W` followed by one or more word characters (`\w` = `[a-zA-Z0-9_]`). In `"Hello, World!"`, the match is `"World"` (the `!` is not `\w`). `.group()` returns the matched string.

---

## Q88. What exception is raised by `my_list[10]` when the list has 5 elements?
- A) `KeyError`
- B) `ValueError`
- C) ✅ **`IndexError`**
- D) `OutOfBoundsError`

📝 **Explanation:** When you access an index **out of range** for a list, string, or tuple, Python raises `IndexError: list index out of range`. Dictionary invalid access raises `KeyError`, not `IndexError`.

---

## Q89. What does `zip()` produce?
```python
names = ["Alice", "Bob"]
scores = [90, 85]
print(list(zip(names, scores)))
```
- A) ✅ **`[('Alice', 90), ('Bob', 85)]`**
- B) `{'Alice': 90, 'Bob': 85}`
- C) `['Alice', 'Bob', 90, 85]`
- D) `[['Alice', 90], ['Bob', 85]]`

📝 **Explanation:** `zip()` **aggregates elements** from multiple iterables into tuples, stopping at the shortest iterable. Result: `[('Alice', 90), ('Bob', 85)]`.

---

## Q90. What is MRO in Python OOP?
- A) Multiple Runtime Objects
- B) ✅ **Method Resolution Order — the order Python searches for a method in class hierarchy**
- C) Memory Reference Object
- D) Module Registration Order

📝 **Explanation:** **Method Resolution Order (MRO)** determines which class's method gets called in an inheritance chain (especially in multiple inheritance). Python uses the **C3 linearization algorithm**. Inspect it with `ClassName.__mro__`.

---

## Q91. What is the output?
```python
try:
    x = int("abc")
except ValueError as e:
    print(f"Caught: {e}")
except Exception:
    print("Generic exception")
```
- A) `Generic exception`
- B) ✅ **`Caught: invalid literal for int() with base 10: 'abc'`**
- C) Both lines print
- D) `TypeError`

📝 **Explanation:** `int("abc")` raises `ValueError`. Python checks handlers **in order** — `ValueError` matches first. The `Exception` block is skipped. `as e` captures the exception message.

---

## Q92. What must a custom exception class inherit from?
- A) `object`
- B) `RuntimeError`
- C) ✅ **`Exception` (or any of its subclasses)**
- D) Nothing — just define a class

📝 **Explanation:** Custom exceptions must inherit from `Exception` (or a more specific built-in). This allows them to be caught by `except Exception` and fit into Python's exception hierarchy. Inheriting from `object` would not make it catchable as an exception.

---

## Q93. What is the output?
```python
words = ["apple", "banana", "kiwi", "fig"]
long_words = [w for w in words if len(w) > 4]
print(long_words)
```
- A) `["kiwi", "fig"]`
- B) ✅ **`['apple', 'banana']`**
- C) `['banana']`
- D) `['apple', 'banana', 'kiwi']`

📝 **Explanation:** Filtered list comprehension: keep words where `len(w) > 4`. `"apple"` (5) ✅, `"banana"` (6) ✅, `"kiwi"` (4) ❌, `"fig"` (3) ❌. Result: `['apple', 'banana']`.

---

## Q94. What does `csv.DictReader` do?
- A) Writes dictionaries to a CSV file
- B) ✅ **Reads each CSV row as a dictionary with column headers as keys**
- C) Converts CSV to JSON format
- D) Reads only the header row

📝 **Explanation:** `csv.DictReader` reads each CSV row into a **Python `dict`**, using the first row (headers) as keys. You access values by column name (e.g., `row["price"]`) instead of index — much more readable.

---

## Q95. What is the output?
```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

shapes = [Shape(), Circle(5)]
for s in shapes:
    print(s.area())
```
- A) `0` only
- B) ✅ **`0` then `78.5`**
- C) `78.5` only
- D) `AttributeError`

📝 **Explanation:** This demonstrates **runtime polymorphism**. When `s.area()` is called, Python calls the appropriate `area()` method based on the **actual object type** at runtime — `0` for `Shape`, `78.5` for `Circle(5)`.

---

## Q96. What keyword manually raises an exception in Python?
```python
if age < 0:
    _____ ValueError("Age cannot be negative")
```
- A) `throw`
- B) `error`
- C) ✅ **`raise`**
- D) `trigger`

📝 **Explanation:** Python uses `raise` to manually throw an exception. `raise ValueError("message")` creates and immediately throws a `ValueError`. Unlike Java/C++ which use `throw`, Python uses `raise`.

---

## Q97. What does `conn.commit()` do in SQLite?
- A) Closes the database connection
- B) ✅ **Permanently saves pending changes (INSERT/UPDATE/DELETE) to the database**
- C) Starts a new transaction
- D) Rolls back the last operation

📝 **Explanation:** SQLite operations run inside an implicit **transaction** that is **not saved until you call `commit()`**. Without it, changes are lost when the connection closes. `rollback()` discards uncommitted changes.

---

## Q98. What is the output?
```python
def apply(func, value):
    return func(value)

result = apply(lambda x: x * 2, 5)
print(result)
```
- A) `5`
- B) `lambda x: x * 2`
- C) ✅ **`10`**
- D) `TypeError`

📝 **Explanation:** Functions are **first-class objects** in Python — they can be passed as arguments. `apply(lambda x: x * 2, 5)` calls the lambda with `5`, returning `10`. This is a fundamental functional programming concept.

---

## Q99. What is the difference between `__str__` and `__repr__`?
- A) They are identical
- B) ✅ **`__str__` is user-friendly; `__repr__` is developer-friendly and unambiguous**
- C) `__repr__` is for printing; `__str__` is for debugging
- D) `__str__` is for numbers; `__repr__` is for strings

📝 **Explanation:** `__str__` provides a **readable** representation for end users (called by `print()` and `str()`). `__repr__` provides an **unambiguous** developer representation (called by `repr()` and in interactive shells).

---

## Q100. What does the `**kwargs` parameter collect?
```python
def show(**kwargs):
    print(kwargs)

show(name="Alice", age=25)
```
- A) A tuple of keyword arguments
- B) ✅ **A dictionary of keyword arguments: `{'name': 'Alice', 'age': 25}`**
- C) A list of keyword arguments
- D) `SyntaxError`

📝 **Explanation:** `**kwargs` collects all **extra keyword arguments** into a **dictionary**. The keys are the parameter names, values are the passed values. Output: `{'name': 'Alice', 'age': 25}`.

---

---

# 🔴 SECTION 3: HARD (Questions 101–150)
> *Topics: Advanced OOP, Iterators, Generators, Decorators, NumPy, Pandas, Flask REST API, Web Scraping, Advanced SQLite, RegEx Groups, Closures, Metaclasses*

---

## Q101. What is the output of this code?
```python
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for num in MyIterator(1, 4):
    print(num, end=" ")
```
- A) `1 2 3 4`
- B) ✅ **`1 2 3`**
- C) `0 1 2 3`
- D) `StopIteration error`

📝 **Explanation:** This is the **iterator protocol**. `__iter__` returns `self`, `__next__` returns the next value or raises `StopIteration` (which stops the `for` loop). Range is `1` to `<4`, so outputs `1 2 3`.

---

## Q102. What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
```
- A) `1 2 3`
- B) ✅ **`1` then `2`**
- C) `[1, 2, 3]`
- D) `StopIteration`

📝 **Explanation:** `yield` makes `gen()` a **generator function**. `next(g)` resumes execution until the next `yield`. First `next(g)` → `1`, second → `2`. The generator preserves state between calls.

---

## Q103. What is the correct HTTP status code for "Resource Created Successfully"?
- A) `200 OK`
- B) ✅ **`201 Created`**
- C) `204 No Content`
- D) `202 Accepted`

📝 **Explanation:** RESTful convention: `200 OK` for successful GET/PUT/DELETE, **`201 Created`** for successful POST (new resource created), `204 No Content` when action succeeded but nothing to return in body.

---

## Q104. What does this Flask route annotation mean?
```python
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    ...
```
- A) Accepts any string as `product_id`
- B) ✅ **Accepts only integer values in the URL, automatically converting to Python `int`**
- C) Makes `product_id` optional
- D) Only matches positive even integers

📝 **Explanation:** Flask's **typed URL converters** validate and convert path variables. `<int:product_id>` ensures the URL segment is a positive integer, auto-converted to Python `int`. Non-integer URLs return 404.

---

## Q105. What is the output?
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])
```
- A) `[True True True False False]`
- B) ✅ **`[4 5]`**
- C) `[3, 4, 5]`
- D) `IndexError`

📝 **Explanation:** `arr > 3` creates a **boolean mask** `[False, False, False, True, True]`. Using this as an index is **boolean indexing** — it returns only the elements where the mask is `True`: `[4, 5]`.

---

## Q106. What does `re.sub()` return?
```python
import re
result = re.sub(r"\d+", "NUM", "I have 3 cats and 12 dogs")
print(result)
```
- A) Finds all digits
- B) ✅ **`I have NUM cats and NUM dogs`**
- C) Splits the string at digits
- D) Returns a list of digit positions

📝 **Explanation:** `re.sub(pattern, replacement, string)` **substitutes** all occurrences of the pattern with the replacement string. All digit sequences (`\d+`) are replaced with `"NUM"`.

---

## Q107. What is a generator expression vs list comprehension?
```python
gen = (x**2 for x in range(5))
lst = [x**2 for x in range(5)]
```
- A) They are identical in all ways
- B) ✅ **Generator is lazy (computes on demand, less memory); list stores all values immediately**
- C) Generator creates a list; list creates a generator
- D) Generator is faster for all operations

📝 **Explanation:** A **generator expression** (parentheses) creates a lazy iterator — values are computed **one at a time** on demand. A **list comprehension** (brackets) computes and stores **all values at once** in memory. Generators are more memory-efficient for large datasets.

---

## Q108. What is the output?
```python
import pandas as pd
data = {"Name": ["Alice", "Bob", "Charlie"], "Score": [90, 85, 92]}
df = pd.DataFrame(data)
print(df["Score"].mean())
```
- A) `90`
- B) ✅ **`89.0`**
- C) `267`
- D) `[90, 85, 92]`

📝 **Explanation:** `df["Score"]` selects the Score column as a Pandas Series. `.mean()` computes the **arithmetic mean**: `(90 + 85 + 92) / 3 = 267 / 3 = 89.0`. Pandas returns a float.

---

## Q109. What does `@app.errorhandler(404)` do in Flask?
- A) Creates a 404 route
- B) ✅ **Registers a custom function to handle 404 Not Found errors**
- C) Raises a 404 error manually
- D) Logs all 404 errors

📝 **Explanation:** `@app.errorhandler(status_code)` registers a **custom error handler**. In REST APIs, this ensures error responses return **JSON** (not Flask's default HTML error pages), maintaining consistent API responses.

---

## Q110. What is the output?
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```
- A) `Hello, Alice` only
- B) `Before` and `After` only
- C) ✅ **`Before`, `Hello, Alice`, `After`**
- D) `SyntaxError`

📝 **Explanation:** `@decorator` is **syntactic sugar** for `greet = decorator(greet)`. When `greet("Alice")` is called, it runs `wrapper("Alice")`: prints "Before", calls original `greet`, prints "After".

---

## Q111. What does `df.groupby("City").agg({"Sales": "sum"})` do in Pandas?
- A) Sorts the DataFrame by City
- B) ✅ **Groups rows by unique City values and computes the sum of Sales for each group**
- C) Filters rows where City equals "Sales"
- D) Creates a pivot table

📝 **Explanation:** `groupby()` splits the DataFrame into groups by unique `"City"` values. `.agg({"Sales": "sum"})` computes the **sum of Sales** for each city group. Fundamental for data analysis and reporting.

---

## Q112. What is the difference between GET and POST in REST APIs?
- A) GET sends data in body; POST sends in URL
- B) ✅ **GET is safe+idempotent (read-only); POST creates resources and is NOT idempotent**
- C) They are interchangeable
- D) GET requires authentication; POST does not

📝 **Explanation:** **GET** is **safe** (read-only) and **idempotent** (same result every time). **POST** creates new resources — calling it twice creates two resources, so it's **not idempotent**. POST data goes in the request body; GET data in the URL query string.

---

## Q113. What is the output?
```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)
```
- A) `[[5, 12], [21, 32]]` (element-wise)
- B) ✅ **`[[19, 22], [43, 50]]` (matrix multiplication)**
- C) `[[6, 8], [10, 12]]`
- D) `TypeError`

📝 **Explanation:** `@` in NumPy performs **matrix multiplication** (dot product). `a @ b`: `(1×5+2×7)=19`, `(1×6+2×8)=22`, `(3×5+4×7)=43`, `(3×6+4×8)=50`. Result: `[[19, 22], [43, 50]]`.

---

## Q114. What is the security concern with `pickle.load()` from untrusted data?
- A) It's slow for large files
- B) It can only load Python 2 objects
- C) ✅ **Malicious pickle data can execute arbitrary code on the machine during deserialization**
- D) It corrupts the original file

📝 **Explanation:** Pickle uses `__reduce__` during unpickling, which can be **exploited to execute arbitrary system commands**. Never unpickle data received from untrusted/public network sources. Use JSON for safe data exchange.

---

## Q115. What does this NumPy code output?
```python
import numpy as np
arr = np.zeros((2, 3))
print(arr.shape)
```
- A) `6`
- B) `[0, 0, 0, 0, 0, 0]`
- C) ✅ **`(2, 3)`**
- D) `2 rows, 3 columns`

📝 **Explanation:** `np.zeros((2, 3))` creates a 2×3 array of zeros. `.shape` returns the **dimensions as a tuple**: `(rows, columns)` = `(2, 3)`. For a 1D array of 5 elements, shape would be `(5,)`.

---

## Q116. In Flask REST APIs, what does `request.get_json(silent=True)` return if the body is invalid JSON?
- A) Raises `json.JSONDecodeError`
- B) Returns an empty dict `{}`
- C) ✅ **Returns `None`**
- D) Returns the raw string body

📝 **Explanation:** `silent=True` suppresses exceptions. If the body is missing or has invalid JSON, `get_json(silent=True)` returns **`None`** instead of raising an exception. You should then check `if payload is None` and return a 400 error.

---

## Q117. What is the output of this nested list comprehension?
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
```
- A) `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- B) ✅ **`[1, 2, 3, 4, 5, 6, 7, 8, 9]`**
- C) `[1, 4, 7, 2, 5, 8, 3, 6, 9]`
- D) `TypeError`

📝 **Explanation:** A **nested list comprehension** with two `for` clauses flattens a 2D list. The outer `for row in matrix` iterates over rows; the inner `for num in row` iterates over elements, collecting all into a flat list.

---

## Q118. What is the output?
```python
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))
```
- A) `15`
- B) `25`
- C) ✅ **`120`**
- D) `RecursionError`

📝 **Explanation:** This is **memoization** — a decorator that caches function results. `factorial(5) = 5! = 120`. The `@memoize` decorator stores results in `cache` to avoid redundant recursive calls.

---

## Q119. In REST API design, which HTTP method is IDEMPOTENT but NOT safe?
- A) `GET`
- B) `POST`
- C) ✅ **`DELETE`**
- D) `PATCH`

📝 **Explanation:** **Idempotent** = same result if called N times. **Safe** = no side effects. `DELETE` is idempotent (deleting twice leaves same state) but NOT safe (modifies server state). `GET` is both safe and idempotent. `POST` is neither.

---

## Q120. What is the output?
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
```
- A) `False`
- B) ✅ **`True`**
- C) `TypeError`
- D) Prints the memory address

📝 **Explanation:** This implements the **Singleton design pattern** using `__new__`. The class-level `_instance` stores the single instance. Both `s1` and `s2` return the **same object** (same memory). `s1 is s2` checks identity → `True`.

---

## Q121. What is the output?
```python
import pandas as pd
df = pd.DataFrame({"A": [1, 2, None, 4], "B": [5, None, 7, 8]})
print(df.isnull().sum())
```
- A) `0` for both columns
- B) `True True`
- C) ✅ **`A: 1, B: 1` (each column has 1 null)**
- D) `TypeError`

📝 **Explanation:** `df.isnull()` creates a boolean DataFrame (True where null). `.sum()` on boolean columns counts `True` values. Column A has 1 `None`, column B has 1 `None`.

---

## Q122. What are Python descriptors?
- A) Comments that describe what a class does
- B) ✅ **Objects that define `__get__`, `__set__`, or `__delete__` to customize attribute access**
- C) A type of decorator applied at the module level
- D) Built-in metaclass features

📝 **Explanation:** **Descriptors** customize **how attribute access works** on class instances. By implementing `__get__`, `__set__`, and/or `__delete__`, a descriptor can intercept attribute lookups. `@property` is internally implemented as a descriptor.

---

## Q123. What does `pd.merge(df1, df2, on="customer_id", how="left")` do?
- A) Concatenates df1 and df2 vertically
- B) ✅ **LEFT JOIN: keeps all rows from df1, matches with df2 on `customer_id`**
- C) Only keeps rows that exist in both DataFrames
- D) Sorts both DataFrames by customer_id

📝 **Explanation:** `pd.merge()` is like SQL JOIN. `how="left"` performs a **LEFT JOIN** — all rows from `df1` are kept; matching rows from `df2` are merged; non-matching rows get NaN in `df2` columns.

---

## Q124. What is the output?
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 4))
```
- A) `7`
- B) ✅ **`14`**
- C) `14 14`
- D) `TypeError`

📝 **Explanation:** The decorator wraps `add` and **doubles its return value**. `add(3, 4)` calls `wrapper(3, 4)`, which calls original `add(3, 4) = 7`, then returns `7 * 2 = 14`.

---

## Q125. What happens when `re.match()` is used on a string that doesn't start with the pattern?
```python
import re
result = re.match(r"\d+", "abc123")
print(result)
```
- A) Returns `"123"`
- B) Raises an exception
- C) ✅ **Returns `None`**
- D) Returns `False`

📝 **Explanation:** `re.match()` only matches at the **beginning** of the string. `"abc123"` doesn't start with digits, so it returns `None`. Use `re.search()` to find the pattern anywhere in the string.

---

## Q126. What does `cursor.executemany()` do in SQLite?
- A) Executes multiple different SQL statements
- B) ✅ **Executes the same parameterized SQL repeatedly with different data tuples (batch insert)**
- C) Fetches multiple rows at once
- D) Runs a SQL script from a file

📝 **Explanation:** `executemany(sql, seq)` runs the same SQL (like INSERT) many times with different parameter tuples. Far more efficient than calling `execute()` in a Python loop, as the driver can optimize the batch.

---

## Q127. What is the output?
```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))
```
- A) `[4, 10, 18]`
- B) `[5, 7, 9]`
- C) ✅ **`32`**
- D) `TypeError`

📝 **Explanation:** `np.dot()` on 1D arrays computes the **dot product (scalar)**. `(1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32`. For 2D arrays, it performs matrix multiplication.

---

## Q128. What is the purpose of `conn.row_factory = sqlite3.Row` in SQLite?
- A) Makes rows return as lists
- B) ✅ **Allows accessing columns by name (`row["column_name"]`) instead of only by index**
- C) Speeds up query execution
- D) Enables foreign key support

📝 **Explanation:** By default, `sqlite3` returns rows as plain **tuples** — access values by index (`row[0]`). Setting `row_factory = sqlite3.Row` makes rows support **both index and column-name access**: `row["customer_id"]`. Much more readable.

---

## Q129. What design pattern does this code implement?
```python
class AbstractShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Square(AbstractShape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
```
- A) Multiple inheritance
- B) ✅ **Template method / Abstract class pattern**
- C) Operator overloading
- D) A mixin pattern

📝 **Explanation:** This is the **abstract class pattern**. The base class defines an interface (method signature) and raises `NotImplementedError` to force subclasses to implement it. Python's `abc` module provides `ABC` and `@abstractmethod` for this formally.

---

## Q130. What does `df.pivot_table(values="Sales", index="Month", aggfunc="sum")` do?
- A) Sorts the DataFrame by Month
- B) ✅ **Creates a summary table showing total Sales grouped by each unique Month**
- C) Creates a new column called "pivot"
- D) Filters rows where Month is not null

📝 **Explanation:** `pivot_table()` is like Excel pivot tables. It **reshapes** the DataFrame by grouping rows by `index` values and computing aggregations on `values`. Here it sums Sales per month.

---

## Q131. What does this code print?
```python
class Meta(type):
    def __new__(mcs, name, bases, attrs):
        attrs["greeting"] = "Hello from Meta!"
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

print(MyClass.greeting)
```
- A) `AttributeError`
- B) ✅ **`Hello from Meta!`**
- C) `None`
- D) `TypeError`

📝 **Explanation:** A **metaclass** controls class creation. `Meta.__new__` is called when `MyClass` is created, automatically adding `greeting` as a class attribute. This is **metaprogramming**. Metaclasses are used in frameworks like Django's ORM.

---

## Q132. What is the output?
```python
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add.__name__)
```
- A) `wrapper`
- B) ✅ **`add`**
- C) `debug`
- D) `__name__`

📝 **Explanation:** `@wraps(func)` from `functools` **preserves the original function's metadata** (name, docstring, etc.) in the wrapper. Without `@wraps`, `add.__name__` would return `"wrapper"`. With it, `"add"` is preserved.

---

## Q133. What does `df.dropna()` do in Pandas?
- A) Drops all numeric columns
- B) ✅ **Removes rows containing any NaN (null) values**
- C) Fills NaN values with 0
- D) Drops duplicate rows

📝 **Explanation:** `df.dropna()` removes **rows with any NaN values** by default. Use `axis=1` to drop columns instead. `df.fillna(value)` fills NaN. `df.dropna(subset=["col"])` only drops rows where a specific column is NaN.

---

## Q134. What is the output?
```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
print([next(gen) for _ in range(7)])
```
- A) `[0, 1, 1, 2, 3, 5, 8, 13]`
- B) ✅ **`[0, 1, 1, 2, 3, 5, 8]`**
- C) `[1, 1, 2, 3, 5, 8, 13]`
- D) `RecursionError`

📝 **Explanation:** An **infinite generator** for Fibonacci numbers. `yield a` pauses and returns `a`. `a, b = b, a + b` updates for the next call. 7 calls return the first 7 Fibonacci numbers: `0, 1, 1, 2, 3, 5, 8`.

---

## Q135. In BeautifulSoup web scraping, what does `soup.find_all("a")` do?
- A) Finds the first anchor tag
- B) ✅ **Returns a list of ALL `<a>` anchor tags in the HTML document**
- C) Finds elements with attribute named "a"
- D) Searches for elements with class "a"

📝 **Explanation:** `find_all(tag)` returns **all matching tags** as a list of `Tag` objects. `soup.find("a")` returns only the first. Access attributes: `tag["href"]`, text content: `tag.text` or `tag.get_text()`.

---

## Q136. What is the output?
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
```
- A) `TypeError: unsupported operand type`
- B) `v1v2`
- C) ✅ **`(4, 6)`**
- D) `Vector object`

📝 **Explanation:** `__add__` is the **operator overloading dunder** for `+`. `v1 + v2` calls `v1.__add__(v2)`, creating `Vector(1+3, 2+4) = Vector(4, 6)`. `print()` calls `__str__`, outputting `(4, 6)`.

---

## Q137. What does `pd.read_csv("file.csv", usecols=["Name", "Age"])` do?
- A) Reads the file but ignores those columns
- B) Creates a new CSV with only those columns
- C) ✅ **Loads ONLY the specified columns from the CSV, ignoring all others**
- D) Filters rows where Name or Age match a pattern

📝 **Explanation:** `usecols` is a **performance optimization** — it tells Pandas to load only the specified columns, saving memory and time when dealing with wide CSVs containing many columns you don't need.

---

## Q138. What is "idempotency" in REST APIs?
- A) An endpoint that requires authentication
- B) ✅ **Calling the same endpoint N times produces the same server state as calling it once**
- C) An endpoint that returns cached responses
- D) An endpoint that only accepts GET requests

📝 **Explanation:** **Idempotency** means N identical calls have the same effect as 1 call on the server state. `GET`, `PUT`, `DELETE` are idempotent. `POST` is NOT (creates a new resource each time).

---

## Q139. What is the output?
```python
class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Database:
    def save(self, data):
        return f"Saved: {data}"

class LoggedDatabase(LogMixin, Database):
    def save(self, data):
        self.log(f"Saving {data}")
        return super().save(data)

db = LoggedDatabase()
print(db.save("record"))
```
- A) `Saved: record` only
- B) `[LOG] Saving record` only
- C) ✅ **`[LOG] Saving record` then `Saved: record`**
- D) `AttributeError`

📝 **Explanation:** This demonstrates the **Mixin pattern**. When `save()` is called, it logs, then calls `super().save(data)` which via MRO finds `Database.save()`, returning `"Saved: record"`. Both outputs appear.

---

## Q140. What does `numpy.where(condition, x, y)` do?
- A) Finds indices where condition is True
- B) ✅ **Returns elements from `x` where condition is True, else from `y` — vectorized conditional**
- C) Returns `True` or `False` for each element
- D) Filters the array based on condition

📝 **Explanation:** `np.where(condition, x, y)` is a **vectorized if-else**. For each position: if `condition` is `True`, take from `x`; otherwise from `y`. Example: `np.where(arr > 0, arr, 0)` zeroes out negative values.

---

## Q141. What is the output?
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))
print(add5(10))
```
- A) `TypeError`
- B) ✅ **`8` then `15`**
- C) `NameError: x is not defined`
- D) `5 5`

📝 **Explanation:** This is a **closure with partial application**. `outer(5)` returns `inner` which **remembers** `x=5` from the enclosing scope. `add5(3)` = `5+3 = 8`. `add5(10)` = `5+10 = 15`. The `x=5` persists across calls.

---

## Q142. In Flask, what is the difference between `jsonify()` and `json.dumps()`?
- A) They are identical
- B) ✅ **`jsonify()` automatically sets `Content-Type: application/json`; `json.dumps()` returns a plain string**
- C) `json.dumps()` is faster for large objects
- D) `jsonify()` can only serialize dictionaries

📝 **Explanation:** `json.dumps()` returns a **plain string**; Flask returns it with `Content-Type: text/html`. `flask.jsonify()` sets the proper **`Content-Type: application/json`** header, supports status code tuples, and respects Flask's JSON settings.

---

## Q143. What is the output?
```python
import numpy as np
arr = np.arange(12).reshape(3, 4)
print(arr[:, 1])
```
- A) `[0, 1, 2, 3]` (first row)
- B) `[4, 5, 6, 7]` (second row)
- C) ✅ **`[1, 5, 9]` (second column)**
- D) `[0, 4, 8]` (first column)

📝 **Explanation:** `np.arange(12).reshape(3, 4)` creates `[[0,1,2,3],[4,5,6,7],[8,9,10,11]]`. `[:, 1]` selects **all rows** from **column 1**: values `1`, `5`, `9`.

---

## Q144. What does this regex capture group do?
```python
import re
pattern = r"(\d{3})-(\d{4})"
match = re.search(pattern, "Call 123-4567 now")
print(match.group(1))
print(match.group(2))
```
- A) Prints the full match twice
- B) ✅ **Prints `123` then `4567` (individual capture groups)**
- C) Prints `123-4567` twice
- D) `AttributeError`

📝 **Explanation:** Parentheses `()` in regex create **capture groups**. `group(0)` = full match (`"123-4567"`), `group(1)` = first capture (`"123"`), `group(2)` = second capture (`"4567"`). Use capture groups to extract specific parts of a match.

---

## Q145. What is Python's GIL (Global Interpreter Lock)?
- A) A security feature preventing external code execution
- B) ✅ **A mutex that allows only one thread to execute Python bytecode at a time**
- C) A garbage collection mechanism
- D) A global variable scope restriction

📝 **Explanation:** The **GIL** is CPython's mechanism ensuring only **one thread executes Python bytecode at a time**. This simplifies memory management but limits true CPU parallelism with threads. Use `multiprocessing` for CPU tasks, `asyncio` for I/O concurrency.

---

## Q146. What is the output?
```python
class DataValidator:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def __call__(self, value):
        return self.min_val <= value <= self.max_val

is_valid_age = DataValidator(0, 150)
print(is_valid_age(25))
print(is_valid_age(-5))
```
- A) `True True`
- B) `False False`
- C) ✅ **`True` then `False`**
- D) `TypeError: object is not callable`

📝 **Explanation:** `__call__` makes an **object callable** like a function! `is_valid_age(25)` calls `DataValidator.__call__(self, 25)`. `0 <= 25 <= 150` is `True`. `0 <= -5 <= 150` is `False`.

---

## Q147. What does `pd.concat([df1, df2], axis=0)` do?
- A) Merges df1 and df2 on a common column (SQL JOIN)
- B) ✅ **Stacks df1 and df2 vertically (row-wise concatenation)**
- C) Creates a cross-join of both DataFrames
- D) Transposes and concatenates

📝 **Explanation:** `pd.concat()` with `axis=0` (default) concatenates **vertically** (stacks df2 rows below df1). `axis=1` concatenates **horizontally** (adds columns side by side). Unlike `merge()`, no common key column is required.

---

## Q148. What is the output?
```python
class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")
        obj.__dict__[self.name] = value

class Product:
    price = Descriptor()
    stock = Descriptor()

p = Product()
p.price = 100
print(p.price)
```
- A) `0`
- B) ✅ **`100`**
- C) `AttributeError`
- D) `ValueError`

📝 **Explanation:** This implements a **data descriptor** with validation. `__set__` validates non-negative values before storing. `__get__` retrieves the value. Setting `p.price = 100` passes validation → stored. `p.price` → returns `100`.

---

## Q149. What does this Flask code demonstrate?
```python
@app.route("/api/v1/products/<int:product_id>", methods=["PATCH"])
def patch_product(product_id):
    body = request.get_json(silent=True)
    allowed_fields = {"name", "price", "stock"}
    update_fields = {k: v for k, v in body.items() if k in allowed_fields}
    # ... build dynamic SQL UPDATE and execute
```
- A) Full replacement of a product (PUT semantics)
- B) ✅ **Partial update — only the provided fields are updated, others untouched**
- C) Creating a new product
- D) Deleting specific product fields

📝 **Explanation:** **PATCH** is for **partial updates** — only the fields in the request body are changed; others remain untouched. Different from **PUT** (full replacement). The whitelist `allowed_fields` prevents arbitrary column injection into SQL.

---

## Q150. What is the output of this advanced code?
```python
def make_counter(step=1):
    def counter():
        n = 0
        while True:
            yield n
            n += step
    return counter()

c1 = make_counter(step=2)
c2 = make_counter(step=5)

print(next(c1))
print(next(c1))
print(next(c2))
```
- A) `2, 4, 5`
- B) ✅ **`0, 2, 0`**
- C) `0, 2, 5`
- D) `2, 4, 10`

📝 **Explanation:** `make_counter` is a **factory** returning a **generator** (closure). `c1` has `step=2`: first `next(c1)` → `0`, second → `2`. `c2` is a **separate, independent generator** with `step=5`: `next(c2)` → `0` (its own fresh start). Each generator maintains independent state.

---

---

# 📊 Quick Reference: Topic Coverage

| Day | Topics | Easy Qs | Medium Qs | Hard Qs |
|-----|---------|---------|-----------|---------|
| Day 1 | Syntax, Variables, Operators, I/O, Loops | Q1–Q20 | — | — |
| Day 2 | Strings, Tuples | Q21–Q35 | Q55, Q66 | Q107 |
| Day 3 | Lists | Q16, Q22, Q27, Q39, Q47 | Q54, Q61, Q77 | Q117 |
| Day 4 | Dictionaries, Exception Handling | Q17, Q29, Q33 | Q51, Q57, Q71, Q74, Q91, Q92, Q96 | Q129 |
| Day 5 | Functions, Scopes, Lambda, RegEx | Q7, Q37 | Q52–Q56, Q70, Q72, Q73, Q87, Q98 | Q110, Q118, Q124, Q132, Q141 |
| Day 6 | OOP, Inheritance, Polymorphism | — | Q58–Q60, Q63–Q65, Q67–Q69, Q75, Q78, Q82, Q86, Q90, Q95, Q99, Q100 | Q101, Q120, Q129, Q131, Q136, Q139, Q146, Q148 |
| Day 7 | File I/O, JSON, CSV, Pickle, SQLite | — | Q60, Q62, Q76, Q79–Q81, Q84, Q97 | Q114, Q126, Q128 |
| Day 8 | NumPy, SciPy, Pandas Intro | — | — | Q105, Q108, Q113, Q115, Q127, Q140, Q143 |
| Day 9 | Pandas Advanced, Visualization | — | — | Q108, Q111, Q121, Q123, Q130, Q133, Q137, Q147 |
| Day 10 | Flask REST API, Web Basics | — | Q62, Q79 | Q103, Q104, Q106, Q109, Q112, Q116, Q119, Q138, Q142, Q149 |
| Day 11 | Flask Advanced, Web Scraping, Scrapy | — | — | Q135, Q138, Q149 |

---

# 🎯 Score Interpretation

| Score | Rating |
|-------|--------|
| **130–150 / 150** | 🏆 **Expert Level** — You're fully prepared! Crush that test! |
| **110–129 / 150** | ⭐ **Advanced** — Strong foundation, minor gaps to fill |
| **85–109 / 150** | 📈 **Intermediate** — Good progress, revise Days 5–8 |
| **60–84 / 150** | 📚 **Developing** — Revise Days 1–6 thoroughly |
| **Below 60 / 150** | 🔄 **Beginner** — Start from Day 1 and work through each README |

---

# 💡 Last-Minute Power Tips

1. `input()` **always returns `str`** — cast with `int()` or `float()` when needed
2. **Strings and tuples are immutable** — operations return NEW objects
3. `range(n)` **starts at 0** — `range(5)` = 0, 1, 2, 3, 4 (NOT 5)
4. `//` **floor division** — always rounds DOWN toward negative infinity
5. **LEGB rule** — Local → Enclosing → Global → Built-in
6. `*args` = **tuple**, `**kwargs` = **dictionary**
7. `__init__` = constructor, `__str__` = print, `__len__` = `len()`, `__add__` = `+`
8. `json.dumps()` → Python to string | `json.loads()` → string to Python
9. **`pickle` is NOT safe** for untrusted data — can execute arbitrary code
10. SQLite: **Always `commit()`** after INSERT/UPDATE/DELETE
11. REST: **GET=safe+idempotent, POST=not idempotent, PUT=idempotent, DELETE=idempotent**
12. `re.match()` = **only at string start** | `re.search()` = **anywhere in string**
13. NumPy **boolean indexing**: `arr[arr > 5]` returns elements where condition is True
14. `@property` = getter, `@method.setter` = setter with validation logic
15. **Generators (`yield`)** are lazy — compute on demand, very memory efficient

---

*📌 Prepared for CDAC PGCP-AI Python MCQ Exam | Day 1 → Day 11 Complete Coverage*  
*🎓 Remember: Understand the WHY behind every answer, not just the WHAT!*
