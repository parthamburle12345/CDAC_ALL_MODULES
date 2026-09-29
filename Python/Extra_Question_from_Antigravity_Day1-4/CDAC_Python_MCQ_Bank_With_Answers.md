# 🐍 CDAC AI — Python Module 1: MCQ Practice Bank
### Days 1–4 | 80 Questions (20 per day) | With Answers
#### Bengaluru Campus — Python Fundamentals Exam Prep

---

> **Instructions**
> - Each question has **4 options (A, B, C, D)**.
> - The correct answer is marked as ✅.
> - Cover each option carefully — MCQ traps are common in CDAC exams.
> - Options are designed to test deep understanding, not just memorization.

---

## 📅 DAY 1 MCQs — Python Basics, Operators, Conditionals & Loops

---

**Q1.** What is the output of the following code?
```python
x = 10
y = 3
print(x // y, x % y)
```

- A) `3.33 1`
- B) `3 1` ✅
- C) `3.0 1.0`
- D) `3 0`

> **Explanation**: `//` is floor division (returns int when both operands are int) → `10 // 3 = 3`. `%` is modulo → `10 % 3 = 1`.

---

**Q2.** Which of the following is a valid Python variable name?

- A) `2_count`
- B) `my-variable`
- C) `_total_sum` ✅
- D) `class`

> **Explanation**: Variable names cannot start with a digit, cannot contain hyphens, and cannot be reserved keywords. `_total_sum` starts with underscore and uses only valid characters.

---

**Q3.** What does `type(True + 1)` return?

- A) `<class 'bool'>`
- B) `<class 'str'>`
- C) `<class 'int'>` ✅
- D) `<class 'float'>`

> **Explanation**: In Python, `bool` is a subclass of `int`. `True` has integer value `1`. So `True + 1 = 2`, which is of type `int`.

---

**Q4.** What is the output?
```python
x = 5
print(x ** 2 ** 2)
```

- A) `100`
- B) `625` ✅
- C) `25`
- D) `Error`

> **Explanation**: `**` is right-associative. `2 ** 2 = 4` is computed first, then `5 ** 4 = 625`.

---

**Q5.** What will the following code print?
```python
x = 10
y = 20
z = 30
print(x < y > z)
```

- A) `True`
- B) `False` ✅
- C) `Error`
- D) `None`

> **Explanation**: Python supports chained comparisons. This evaluates as `(x < y) and (y > z)` → `(10 < 20) and (20 > 30)` → `True and False` → `False`.

---

**Q6.** What is the output?
```python
name = input("Enter: ")  # User types: 25
print(type(name))
```

- A) `<class 'int'>`
- B) `<class 'float'>`
- C) `<class 'str'>` ✅
- D) Depends on what the user types

> **Explanation**: `input()` **always** returns a string (`str`), regardless of what the user types.

---

**Q7.** Which value is **Falsy** in Python?

- A) `"False"`
- B) `[0]`
- C) `0.0` ✅
- D) `(False,)`

> **Explanation**: `0.0` (float zero) is Falsy. `"False"` is a non-empty string (Truthy), `[0]` is a non-empty list (Truthy), `(False,)` is a non-empty tuple (Truthy).

---

**Q8.** What is the output?
```python
for i in range(1, 10, 3):
    print(i, end=" ")
```

- A) `1 4 7 10`
- B) `1 4 7` ✅
- C) `1 3 6 9`
- D) `3 6 9`

> **Explanation**: `range(1, 10, 3)` generates: start=1, step=3 → `1, 4, 7` (stops before 10).

---

**Q9.** What will this code print?
```python
count = 0
while count < 5:
    count += 2
print(count)
```

- A) `4`
- B) `5`
- C) `6` ✅
- D) `2`

> **Explanation**: `count` starts at 0, then becomes 2, then 4, then 6. After 6, `6 < 5` is False, so the loop exits. `count` is 6.

---

**Q10.** What is the output?
```python
for i in range(3):
    if i == 2:
        break
    print(i, end=" ")
else:
    print("Done")
```

- A) `0 1 Done`
- B) `0 1 2 Done`
- C) `0 1` ✅
- D) `Done`

> **Explanation**: The loop breaks when `i == 2`, so `2` is never printed. Because `break` was triggered, the `else` block does **not** execute.

---

**Q11.** What is the result of `17 // -3` in Python?

- A) `-5` ✅
- B) `-6`
- C) `5`
- D) `-5.67`

> **Explanation**: Floor division always rounds **down** (towards negative infinity). `17 / -3 = -5.67...`, floor of that = `-6`. Wait — actually: `17 // -3 = -6` is incorrect. Let's recalculate: `-5.666...`, floor towards negative infinity = `-6`. **Correct answer is B) `-6`** ✅

> *(Note to student: `17 // -3` = `-6` because Python's floor division rounds toward negative infinity. `-5.67` floors to `-6`)*

- A) `-5`
- B) `-6` ✅
- C) `5`
- D) `6`

---

**Q12.** Which operator is used for **exponentiation** in Python?

- A) `^`
- B) `^^`
- C) `**` ✅
- D) `pow`

> **Explanation**: `**` is Python's exponentiation operator. `^` is the **bitwise XOR** operator. `pow()` is a built-in function, not an operator.

---

**Q13.** What is printed by this code?
```python
x = 5
if x > 3:
    print("A")
elif x > 4:
    print("B")
else:
    print("C")
```

- A) `A B`
- B) `B`
- C) `A` ✅
- D) `A B C`

> **Explanation**: `x = 5 > 3` is True, so block `A` executes. In an `if-elif-else` chain, **only the first matching block runs**. Even though `x > 4` is also True, it is never evaluated.

---

**Q14.** What is the output?
```python
x = None
if x:
    print("Truthy")
else:
    print("Falsy")
```

- A) `Truthy`
- B) `Falsy` ✅
- C) `None`
- D) `Error`

> **Explanation**: `None` is a Falsy value in Python. The `else` block executes.

---

**Q15.** What is the output of this code?
```python
print(f"{42:08b}")
```

- A) `42`
- B) `00101010` ✅
- C) `101010`
- D) `0b101010`

> **Explanation**: `:08b` formats `42` as binary (`:b`) padded with zeros to width 8. `42` in binary is `101010` → zero-padded to 8 digits → `00101010`.

---

**Q16.** What is the data type of `x` after this code?
```python
x = 5 / 2
```

- A) `int`
- B) `float` ✅
- C) `complex`
- D) `double`

> **Explanation**: In Python 3, the `/` operator **always returns a float**, even if the result is a whole number. `5 / 2 = 2.5` (float).

---

**Q17.** What will this code output?
```python
a, b, c = 1, 2, 3
a, b = b, a
print(a, b, c)
```

- A) `1 2 3`
- B) `2 1 3` ✅
- C) `1 2 1`
- D) Error

> **Explanation**: Python evaluates the right side first (tuple packing), then unpacks: `a = 2`, `b = 1`. `c` is unchanged.

---

**Q18.** What is the purpose of the `pass` statement?

- A) Terminates the current loop iteration
- B) Exits the loop completely
- C) Acts as a no-operation syntactic placeholder ✅
- D) Pauses execution for 1 second

> **Explanation**: `pass` is a null statement used as a placeholder when a code block is syntactically required but you don't want any action to happen.

---

**Q19.** What will `print(10 != 10)` output?

- A) `True`
- B) `False` ✅
- C) `0`
- D) `None`

> **Explanation**: `!=` means "not equal to". `10` is equal to `10`, so `10 != 10` is `False`.

---

**Q20.** What is the output?
```python
x = 0
y = 10
print(x or y)
```

- A) `0`
- B) `False`
- C) `True`
- D) `10` ✅

> **Explanation**: Python's `or` operator doesn't always return a bool. It returns the **first truthy value** it finds, or the last value if none are truthy. `x = 0` is Falsy, so Python evaluates `y = 10` which is Truthy, and returns `10`.

---

## 📅 DAY 2 MCQs — Strings & Tuples

---

**Q21.** What is the output?
```python
s = "Bangalore"
print(s[-4:-1])
```

- A) `lor`
- B) `ore`
- C) `lor` ✅
- D) `galo`

> **Explanation**: `s = "Bangalore"` (indices 0-8). `s[-4]` = index 5 = `'l'`, `s[-1]` = `'e'` (excluded). Slice `[-4:-1]` = `'l','o','r'` = `"lor"`.

---

**Q22.** What happens when you try to execute `s[0] = 'b'` where `s = "Bangalore"`?

- A) `s` becomes `"bangalore"`
- B) `s[0]` is updated to `'b'`
- C) `TypeError` is raised ✅
- D) `AttributeError` is raised

> **Explanation**: Strings are **immutable** in Python. You cannot modify individual characters in-place. Attempting to do so raises a `TypeError`.

---

**Q23.** What is the output?
```python
s = "python"
print(s[::2])
```

- A) `nohtyp`
- B) `pto` ✅
- C) `yhn`
- D) `python`

> **Explanation**: `s[::2]` uses a step of 2, starting from index 0: `s[0]='p'`, `s[2]='t'`, `s[4]='o'` → `"pto"`.

---

**Q24.** What does `"cdac".center(10, "*")` return?

- A) `"***cdac***"`
- B) `"***cdac***"` ✅
- C) `"cdac******"`
- D) `"***cdac***"`

> **Explanation**: `.center(10, "*")` pads the string to width 10, centering it. `"cdac"` is 4 chars, 6 chars of padding → 3 on each side → `"***cdac***"`.

---

**Q25.** What is the output?
```python
words = "   Hello World   "
print(words.strip().split())
```

- A) `['   Hello', 'World   ']`
- B) `['Hello', 'World']` ✅
- C) `['Hello World']`
- D) `['Hello', ' ', 'World']`

> **Explanation**: `.strip()` removes leading/trailing whitespace → `"Hello World"`. `.split()` (no argument) splits on any whitespace and removes empty strings → `['Hello', 'World']`.

---

**Q26.** Which of the following correctly creates a **single-element tuple**?

- A) `t = (5)`
- B) `t = [5]`
- C) `t = (5,)` ✅
- D) `t = tuple[5]`

> **Explanation**: Without the trailing comma, `(5)` is just the integer `5` in parentheses (grouping), not a tuple. The trailing comma `(5,)` tells Python it's a tuple.

---

**Q27.** What is the output?
```python
t = (1, 2, [3, 4])
t[2][0] = 99
print(t)
```

- A) `(1, 2, [99, 4])` ✅
- B) `TypeError`
- C) `(1, 2, [3, 4])`
- D) `(99, 2, [3, 4])`

> **Explanation**: Tuples are immutable — you cannot replace `t[2]` with another object. However, `t[2]` is a **list**, and lists are mutable. You can modify the list's contents in-place. So `t[2][0] = 99` works, giving `(1, 2, [99, 4])`.

---

**Q28.** What does `"AI".join(["CD", "AC"])` return?

- A) `"CDAC"`
- B) `"CDAIAC"` ✅
- C) `"AICDC"`
- D) `"CDAI AC"`

> **Explanation**: `.join(iterable)` inserts the string between each element of the iterable. `"AI".join(["CD", "AC"])` → `"CD" + "AI" + "AC"` = `"CDAIAC"`.

---

**Q29.** What is the output?
```python
a, *b, c = (10, 20, 30, 40, 50)
print(b)
```

- A) `[20, 30, 40]` ✅
- B) `(20, 30, 40)`
- C) `[10, 20, 30, 40]`
- D) `20 30 40`

> **Explanation**: Extended tuple unpacking: `a = 10`, `c = 50`, and `*b` collects all middle elements into a **list**: `[20, 30, 40]`. Note: the result is always a list, even when unpacking a tuple.

---

**Q30.** What is the output?
```python
email = "trainer@cdac.in"
domain = email[email.find("@") + 1:]
print(domain)
```

- A) `"trainer"`
- B) `"@cdac.in"`
- C) `"cdac.in"` ✅
- D) `"cdac"`

> **Explanation**: `email.find("@")` returns `7`. `email[7+1:]` = `email[8:]` = `"cdac.in"`.

---

**Q31.** What is the output?
```python
s = "abcabc"
print(s.count("bc"))
```

- A) `1`
- B) `2` ✅
- C) `3`
- D) `0`

> **Explanation**: `.count(sub)` counts non-overlapping occurrences of `"bc"` in `"abcabc"`. Found at index 1 and index 4 → `2`.

---

**Q32.** Which f-string feature is used for debugging in Python 3.8+?

- A) `f"{var!r}"`
- B) `f"{var=}"` ✅
- C) `f"{var:d}"`
- D) `f"{var:#}"`

> **Explanation**: The `=` specifier inside f-strings (added in Python 3.8) prints both the variable name and its value: `f"{name=}"` → `name='Vinod'`.

---

**Q33.** What will `"Python"[::-1]` produce?

- A) `"Python"`
- B) `"nohtyP"` ✅
- C) `"nohty"`
- D) `"Pytho"`

> **Explanation**: `[::-1]` reverses the entire string by stepping backwards from the last character to the first.

---

**Q34.** What is the output?
```python
t1 = (1, 2, 3)
t2 = t1 * 2
print(len(t2))
```

- A) `3`
- B) `6` ✅
- C) `2`
- D) `Error`

> **Explanation**: `t1 * 2` repeats the tuple twice: `(1, 2, 3, 1, 2, 3)`. Its length is `6`.

---

**Q35.** What does `"  hello  ".lstrip()` return?

- A) `"hello"`
- B) `"hello  "` ✅
- C) `"  hello"`
- D) `"hello"`

> **Explanation**: `.lstrip()` removes whitespace from the **left** side only. The right-side spaces remain: `"hello  "`.

---

**Q36.** What is the output?
```python
s = "Vinod Kumar"
print(s.replace("Kumar", "").strip())
```

- A) `"Vinod Kumar"`
- B) `"Vinod"` ✅
- C) `"Vinod "`
- D) `"Kumar"`

> **Explanation**: `.replace("Kumar", "")` removes `"Kumar"` → `"Vinod "`. `.strip()` removes the trailing space → `"Vinod"`.

---

**Q37.** What is the output?
```python
t = (10, 20, 30, 40, 50)
print(t[1:4])
```

- A) `(20, 30, 40)` ✅
- B) `(10, 20, 30, 40)`
- C) `(20, 30, 40, 50)`
- D) `[20, 30, 40]`

> **Explanation**: Tuple slicing `[1:4]` gives elements at indices 1, 2, 3 → `(20, 30, 40)`. The result is also a tuple, not a list.

---

**Q38.** What does `"cdac".upper().startswith("CD")` return?

- A) `False`
- B) `True` ✅
- C) `Error`
- D) `"CD"`

> **Explanation**: `"cdac".upper()` → `"CDAC"`. `"CDAC".startswith("CD")` → `True`.

---

**Q39.** Which of the following will raise a `ValueError`?

- A) `int("42")`
- B) `float("3.14")`
- C) `int("3.14")` ✅
- D) `str(42)`

> **Explanation**: `int("3.14")` raises a `ValueError` because `"3.14"` is not a valid integer literal. You must first convert it to float: `int(float("3.14"))`.

---

**Q40.** What is the output?
```python
city = "Bangalore"
print(f"{city:>15}")
```

- A) `"Bangalore      "`
- B) `"      Bangalore"` ✅
- C) `"   Bangalore   "`
- D) `"Bangalore"`

> **Explanation**: `>15` means right-align within a field of width 15. `"Bangalore"` is 9 chars, so 6 spaces are added to the left: `"      Bangalore"`.

---

## 📅 DAY 3 MCQs — Lists & List Comprehensions

---

**Q41.** What is the output?
```python
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30, 40]
print(nums)
```

- A) `[1, 20, 30, 40, 5]` ✅
- B) `[1, 20, 30, 40, 4, 5]`
- C) `[20, 30, 40]`
- D) `Error`

> **Explanation**: Slice assignment `nums[1:3] = [20, 30, 40]` **replaces** elements at indices 1 and 2 with three new elements. The list grows from 5 to 6 elements... wait. Let's re-evaluate. `nums[1:3]` selects `[2, 3]` (2 elements). We replace those with `[20, 30, 40]` (3 elements). Result: `[1, 20, 30, 40, 4, 5]`.

- A) `[1, 20, 30, 40, 5]`
- B) `[1, 20, 30, 40, 4, 5]` ✅
- C) `[20, 30, 40]`
- D) `Error`

---

**Q42.** What is the output?
```python
lst = [1, 2, 3]
lst.append([4, 5])
print(len(lst))
```

- A) `5`
- B) `4` ✅
- C) `3`
- D) `2`

> **Explanation**: `.append()` adds the **entire object** `[4, 5]` as a single element (a nested list). The resulting list is `[1, 2, 3, [4, 5]]` with length `4`.

---

**Q43.** What is the difference between `list.append(x)` and `list.extend(x)`?

- A) They are identical
- B) `append` adds all elements of `x`; `extend` adds `x` as a single element
- C) `append` adds `x` as a single element; `extend` adds all elements of `x` ✅
- D) `extend` only works with tuples

> **Explanation**: `.append(x)` appends `x` as **one item** (even if `x` is a list, it becomes a nested list). `.extend(x)` iterates over `x` and adds each element individually.

---

**Q44.** What is the output?
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]` ✅
- C) `[4, 1, 2, 3]`
- D) `Error`

> **Explanation**: `b = a` does **not** create a copy. Both `a` and `b` point to the **same list object** in memory. Modifying via `b` also modifies `a`.

---

**Q45.** What will this list comprehension produce?
```python
result = [x**2 for x in range(5) if x % 2 != 0]
print(result)
```

- A) `[0, 4, 16]`
- B) `[1, 9]` ✅
- C) `[1, 4, 9, 16]`
- D) `[1, 3]`

> **Explanation**: `range(5)` = `[0, 1, 2, 3, 4]`. Filtering `x % 2 != 0` (odd numbers): `[1, 3]`. Squaring them: `[1, 9]`.

---

**Q46.** What is the output?
```python
lst = [3, 1, 4, 1, 5, 9, 2]
lst.sort()
print(lst[0], lst[-1])
```

- A) `3 2`
- B) `1 9` ✅
- C) `9 1`
- D) `3 9`

> **Explanation**: `.sort()` sorts in-place in ascending order: `[1, 1, 2, 3, 4, 5, 9]`. `lst[0] = 1`, `lst[-1] = 9`.

---

**Q47.** What does `lst.pop()` do when called without an argument?

- A) Removes and returns the first element
- B) Removes and returns the last element ✅
- C) Removes all elements
- D) Returns the last element without removing it

> **Explanation**: `list.pop()` without arguments removes and returns the **last** element (index `-1`). `list.pop(0)` removes the first element.

---

**Q48.** What is the output?
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)
```

- A) `[[1, 2], [3, 4], [5, 6]]`
- B) `[1, 2, 3, 4, 5, 6]` ✅
- C) `[[1, 3, 5], [2, 4, 6]]`
- D) `Error`

> **Explanation**: Nested list comprehension: the outer loop iterates rows, the inner loop iterates numbers in each row → flattens the matrix into a single list.

---

**Q49.** What is the output?
```python
lst = [10, 20, 30, 40, 50]
print(lst.index(30))
```

- A) `2` ✅
- B) `3`
- C) `30`
- D) `True`

> **Explanation**: `.index(value)` returns the **index** of the first occurrence of `value`. `30` is at index `2`.

---

**Q50.** How do you create a **shallow copy** of a list `a`?

- A) `b = a`
- B) `b = a.copy()` ✅
- C) `b = list(a)` ✅
- D) Both B and C are correct ✅

> **Explanation**: Both `a.copy()` and `list(a)` create shallow copies. `b = a` merely creates another reference to the **same** list object.

*(Note: In a real exam, if both B and C are listed as separate options, choose "Both B and C".)*

---

**Q51.** What is the output?
```python
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "mango")
print(fruits[2])
```

- A) `"banana"` ✅
- B) `"mango"`
- C) `"cherry"`
- D) `"apple"`

> **Explanation**: `.insert(1, "mango")` inserts `"mango"` at index 1, shifting `"banana"` and `"cherry"` to indices 2 and 3. `fruits[2]` is now `"banana"`.

---

**Q52.** What will this code produce?
```python
x = [i for i in range(10) if i % 3 == 0]
print(x)
```

- A) `[0, 3, 6, 9]` ✅
- B) `[3, 6, 9]`
- C) `[1, 4, 7]`
- D) `[0, 3, 6]`

> **Explanation**: Numbers in range(10) divisible by 3: `0, 3, 6, 9`.

---

**Q53.** What is the output?
```python
lst = [1, 2, 3, 2, 1]
lst.remove(2)
print(lst)
```

- A) `[1, 3, 2, 1]` ✅
- B) `[1, 3, 1]`
- C) `[1, 2, 3, 1]`
- D) `Error`

> **Explanation**: `.remove(value)` removes the **first occurrence** of the value. The first `2` (at index 1) is removed, leaving `[1, 3, 2, 1]`.

---

**Q54.** What is the difference between a list and a tuple?

- A) Lists use `()`, tuples use `[]`
- B) Lists are immutable, tuples are mutable
- C) Lists are mutable, tuples are immutable ✅
- D) There is no difference

> **Explanation**: The fundamental difference: lists are **mutable** (can be changed after creation), tuples are **immutable** (cannot be changed after creation). Lists use `[]`, tuples use `()`.

---

**Q55.** What is the output?
```python
from random import randrange
nums = [randrange(5000) for _ in range(5)]
evens = [n for n in nums if n % 2 == 0]
print(type(evens))
```

- A) `<class 'tuple'>`
- B) `<class 'generator'>`
- C) `<class 'list'>` ✅
- D) `<class 'set'>`

> **Explanation**: A list comprehension `[...]` always produces a `list` object.

---

**Q56.** What is the output?
```python
lst = [1, 2, 3, 4, 5]
print(lst[::–1])
```

- A) `[5, 4, 3, 2, 1]` ✅
- B) `[1, 2, 3, 4, 5]`
- C) `Error`
- D) `[4, 3, 2, 1]`

> **Explanation**: `[::-1]` reverses the list by stepping backwards.

---

**Q57.** What does `del lst[2]` do to `lst = [10, 20, 30, 40]`?

- A) Sets `lst[2]` to `None`
- B) Removes the element at index 2 ✅
- C) Removes all elements equal to `30`
- D) Returns `30` and removes it

> **Explanation**: `del lst[2]` deletes the element at index `2` (which is `30`). The list becomes `[10, 20, 40]`. Unlike `.pop()`, `del` does not return the removed value.

---

**Q58.** What is the output?
```python
data = [5, 3, 8, 1, 9, 2]
data.sort(reverse=True)
print(data[:3])
```

- A) `[1, 2, 3]`
- B) `[9, 8, 5]` ✅
- C) `[5, 8, 9]`
- D) `[8, 5, 3]`

> **Explanation**: After `sort(reverse=True)`, `data = [9, 8, 5, 3, 2, 1]`. `data[:3]` = `[9, 8, 5]`.

---

**Q59.** What is the output?
```python
lst = [1, 2, 3]
result = lst * 2 + [0]
print(result)
```

- A) `[2, 4, 6, 0]`
- B) `[1, 2, 3, 1, 2, 3, 0]` ✅
- C) `[1, 2, 3, 0, 1, 2, 3]`
- D) `[0, 1, 2, 3, 1, 2, 3]`

> **Explanation**: `lst * 2` = `[1, 2, 3, 1, 2, 3]`. Then `+ [0]` concatenates `[0]` at the end → `[1, 2, 3, 1, 2, 3, 0]`.

---

**Q60.** What does `sum([[1,2],[3,4],[5,6]], [])` produce?

- A) `[1, 2, 3, 4, 5, 6]` ✅
- B) `21`
- C) `Error`
- D) `[[1,2],[3,4],[5,6]]`

> **Explanation**: `sum(iterable, start)` with `start=[]` concatenates lists. It does `[] + [1,2] + [3,4] + [5,6]` = `[1,2,3,4,5,6]`. This is a list-flattening trick.

---

## 📅 DAY 4 MCQs — Dictionaries & Exception Handling

---

**Q61.** What is the output?
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.get("d", 0))
```

- A) `None`
- B) `KeyError`
- C) `0` ✅
- D) `d`

> **Explanation**: `.get(key, default)` returns `default` if the key doesn't exist, instead of raising `KeyError`. `"d"` is not in the dict, so `0` is returned.

---

**Q62.** What is the output?
```python
d = {"x": 10, "y": 20}
d["z"] = 30
d["x"] = 100
print(len(d))
```

- A) `2`
- B) `3` ✅
- C) `4`
- D) `Error`

> **Explanation**: After operations: `d = {"x": 100, "y": 20, "z": 30}`. `"x"` was updated (not added again). The dictionary has `3` key-value pairs.

---

**Q63.** What does `d.items()` return?

- A) A list of all keys
- B) A list of all values
- C) A view of `(key, value)` pairs as tuples ✅
- D) A dictionary of all items

> **Explanation**: `.items()` returns a `dict_items` view object containing `(key, value)` tuples. You can iterate over it with `for k, v in d.items():`.

---

**Q64.** What is the output?
```python
d = {"name": "Riya", "city": "Pune"}
k, v = d.popitem()
print(len(d))
```

- A) `2`
- B) `1` ✅
- C) `0`
- D) `Error`

> **Explanation**: `.popitem()` removes and returns the **last inserted** key-value pair (in Python 3.7+, dicts maintain insertion order). One item is removed → length becomes `1`.

---

**Q65.** What is the output?
```python
d = {1: "one", 2: "two", 3: "three"}
result = {k: v.upper() for k, v in d.items() if k % 2 != 0}
print(result)
```

- A) `{1: "ONE", 2: "TWO", 3: "THREE"}`
- B) `{1: "ONE", 3: "THREE"}` ✅
- C) `{"one": 1, "three": 3}`
- D) `{2: "TWO"}`

> **Explanation**: Dict comprehension filters for odd keys (`k % 2 != 0`): keys `1` and `3`. `.upper()` converts values → `{1: "ONE", 3: "THREE"}`.

---

**Q66.** Which of the following can be used as a **dictionary key**?

- A) A list `[1, 2]`
- B) A dictionary `{"a": 1}`
- C) A tuple `(1, 2)` ✅
- D) A set `{1, 2}`

> **Explanation**: Dictionary keys must be **hashable** (immutable). Tuples are immutable and hashable. Lists, dicts, and sets are mutable and unhashable, so they cannot be used as keys.

---

**Q67.** What is the output?
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error!")
finally:
    print("Done")
```

- A) `Error!`
- B) `Done`
- C) `Error!\nDone` ✅
- D) Nothing is printed

> **Explanation**: The `except` block catches `ZeroDivisionError` and prints `"Error!"`. The `finally` block **always executes**, so `"Done"` is also printed. Both lines are printed.

---

**Q68.** What happens when you access a non-existent key using `d["missing_key"]`?

- A) Returns `None`
- B) Returns `0`
- C) Raises `KeyError` ✅
- D) Raises `ValueError`

> **Explanation**: Accessing a key that doesn't exist using square bracket notation raises a `KeyError`. Use `.get()` to avoid this.

---

**Q69.** What is the output?
```python
try:
    x = int("hello")
except ValueError as e:
    print("Caught:", type(e).__name__)
```

- A) `Caught: TypeError`
- B) `Caught: ValueError` ✅
- C) `Error`
- D) Nothing is printed

> **Explanation**: `int("hello")` raises a `ValueError`. The `except ValueError as e` block catches it. `type(e).__name__` gives `"ValueError"`.

---

**Q70.** What is the output?
```python
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 30})
print(d)
```

- A) `{"a": 1, "b": 2, "c": 30}`
- B) `{"a": 1, "b": 20, "c": 30}` ✅
- C) `{"b": 20, "c": 30}`
- D) `Error`

> **Explanation**: `.update()` updates existing keys and adds new ones. `"b"` was updated from `2` to `20`, and `"c": 30` was added.

---

**Q71.** When is the `else` block in a `try-except-else-finally` executed?

- A) Always
- B) Only when an exception is raised
- C) Only when NO exception is raised ✅
- D) Only when `finally` is missing

> **Explanation**: The `else` block in a try-except runs only if the `try` block **completed without raising an exception**. The `finally` block always runs.

---

**Q72.** What is the output?
```python
d = {"scores": [85, 92, 78]}
d["scores"].append(95)
print(d["scores"])
```

- A) `[85, 92, 78]`
- B) `[85, 92, 78, 95]` ✅
- C) `Error`
- D) `{"scores": [85, 92, 78, 95]}`

> **Explanation**: `d["scores"]` returns the list object. `.append(95)` modifies it in-place. The dictionary value is updated because both reference the same list object.

---

**Q73.** What is the output?
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares[4])
```

- A) `4`
- B) `16` ✅
- C) `{4: 16}`
- D) `Error`

> **Explanation**: The dict comprehension creates `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`. `squares[4]` → `16`.

---

**Q74.** What is the output?
```python
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index Error!")
except Exception:
    print("General Error!")
finally:
    print("Finally!")
```

- A) `Index Error!`
- B) `General Error! Finally!`
- C) `Index Error!\nFinally!` ✅
- D) `Finally!`

> **Explanation**: `lst[5]` raises `IndexError` (only 3 elements). The first matching `except` block runs (`"Index Error!"`), then `finally` always runs (`"Finally!"`).

---

**Q75.** Which of the following correctly iterates over only the **values** of a dictionary?

- A) `for k in d:`
- B) `for v in d.values():` ✅
- C) `for v in d.keys():`
- D) `for k, v in d:`

> **Explanation**: `for k in d:` and `for k in d.keys():` iterate over keys. `for k, v in d.items():` iterates over key-value pairs. `for v in d.values():` iterates over values only.

---

**Q76.** What is the output?
```python
d = {"a": 10, "b": 20, "c": 30}
print(d.pop("b"))
print(len(d))
```

- A) `20\n2` ✅
- B) `None\n3`
- C) `b\n2`
- D) `Error`

> **Explanation**: `.pop("b")` removes key `"b"` and **returns its value** `20`. After removal, the dict has 2 entries.

---

**Q77.** Which statement about dictionaries is **FALSE**?

- A) Dictionary keys must be unique
- B) Dictionary values can be duplicated
- C) Dictionary keys must be immutable
- D) Dictionaries are ordered by insertion order in Python 2.7 ✅

> **Explanation**: In **Python 2.7**, dictionaries were **unordered**. Insertion order was guaranteed only from **Python 3.7+**. The statement says "ordered in Python 2.7" which is FALSE.

---

**Q78.** What is the output?
```python
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    result = float('inf')
print(result)
```

- A) `Error`
- B) `0`
- C) `inf` ✅
- D) `None`

> **Explanation**: `10 / 0` raises `ZeroDivisionError`. The `except` block assigns `float('inf')` (positive infinity) to `result`. This prints `inf`.

---

**Q79.** What is the output?
```python
profile = {"name": "Arjun", "age": 25, "city": "Bangalore"}
keys = list(profile.keys())
print(keys[1])
```

- A) `"name"`
- B) `"age"` ✅
- C) `25`
- D) `"city"`

> **Explanation**: In Python 3.7+, dicts maintain insertion order. `profile.keys()` = `["name", "age", "city"]`. `keys[1]` = `"age"`.

---

**Q80.** What is the output?
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Executed")

result = safe_divide(10, 0)
print(result)
```

- A) `Executed\nNone` ✅
- B) `None\nExecuted`
- C) `Executed`
- D) `Error`

> **Explanation**: When `ZeroDivisionError` occurs, the `except` block sets the return value to `None`. BUT `finally` always executes **before the function actually returns**. So `"Executed"` is printed first, then `None` is returned and printed.

---

## 📊 Answer Key Summary

### Day 1 Answers
| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | B   | 6 | C   | 11| B   | 16| B   |
| 2 | C   | 7 | C   | 12| C   | 17| B   |
| 3 | C   | 8 | B   | 13| C   | 18| C   |
| 4 | B   | 9 | C   | 14| B   | 19| B   |
| 5 | B   | 10| C   | 15| B   | 20| D   |

### Day 2 Answers
| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 21| C   | 26| C   | 31| B   | 36| B   |
| 22| C   | 27| A   | 32| B   | 37| A   |
| 23| B   | 28| B   | 33| B   | 38| B   |
| 24| B   | 29| A   | 34| B   | 39| C   |
| 25| B   | 30| C   | 35| B   | 40| B   |

### Day 3 Answers
| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 41| B   | 46| B   | 51| A   | 56| A   |
| 42| B   | 47| B   | 52| A   | 57| B   |
| 43| C   | 48| B   | 53| A   | 58| B   |
| 44| B   | 49| A   | 54| C   | 59| B   |
| 45| B   | 50| D   | 55| C   | 60| A   |

### Day 4 Answers
| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 61| C   | 66| C   | 71| C   | 76| A   |
| 62| B   | 67| C   | 72| B   | 77| D   |
| 63| C   | 68| C   | 73| B   | 78| C   |
| 64| B   | 69| B   | 74| C   | 79| B   |
| 65| B   | 70| B   | 75| B   | 80| A   |

---

## 🎯 Exam Tips for CDAC MCQs

1. **Tricky `input()`**: Always returns `str` — a very common MCQ trap.
2. **`//` on negatives**: Python floors toward negative infinity — `(-10 // 3) = -4`, not `-3`.
3. **`bool` is a subclass of `int`**: `True == 1`, `False == 0`, and `True + 1 == 2`.
4. **Mutable default arguments**: Common gotcha in functions with mutable defaults.
5. **`in` operator on dicts**: `"key" in d` checks **keys only**, not values.
6. **`finally` always runs**: Even after `return` — it executes before the function returns.
7. **Tuple with one element needs trailing comma**: `(5,)` is a tuple; `(5)` is an int.
8. **List `b = a` vs `b = a.copy()`**: The former is aliasing; modifying one affects both.
9. **`or` / `and` return values, not booleans**: `0 or "hello"` returns `"hello"`.
10. **`f"{x=}"`** (Python 3.8+): Prints both the expression and its value — a debugging trick.

---

*Prepared for CDAC AI — Python Module 1 | Bengaluru Campus | August 2026*
