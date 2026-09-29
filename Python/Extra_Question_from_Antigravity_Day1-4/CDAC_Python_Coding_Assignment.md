# 🐍 CDAC AI — Python Module 1: Coding Assignment
### Days 1–4 | 20 Questions (5 per day)
#### Bengaluru Campus — Python Fundamentals Practice

---

> **Instructions**
> - Solve each question by writing a complete Python program in a separate `.py` file.
> - Use **meaningful variable names** and add **comments** to explain your logic.
> - Ensure your program handles edge cases (invalid input, empty values, etc.) where specified.
> - Follow **PEP 8** naming conventions (`snake_case` for variables and functions).

---

## 📅 DAY 1 — Variables, Operators, Conditionals & Loops

> **Topics Tested**: Data types (int, float, bool, NoneType), arithmetic/comparison/logical operators,
> `input()` / `print()` / f-strings, `if-elif-else`, `while`, `for`, `range()`, `break`, `continue`, `pass`

---

### Q1. 🔢 Digital Root Calculator

The **digital root** of a number is obtained by repeatedly summing its digits until only a single digit remains.

- Prompt the user for a positive integer.
- Repeatedly sum all digits of the number until only a single digit remains.
- Print the digital root and how many **reduction steps** it took.

**Sample Input:** `9875`
**Sample Output:**
```
Original number : 9875
Step 1          : 9 + 8 + 7 + 5 = 29
Step 2          : 2 + 9 = 11
Step 3          : 1 + 1 = 2
Digital Root    : 2
Total Steps     : 3
```

---

### Q2. 🧮 Quadratic Equation Solver

A quadratic equation is of the form: **ax² + bx + c = 0**

- Prompt the user to enter three coefficients `a`, `b`, and `c` (can be floats).
- Compute the **discriminant** `D = b² - 4ac`.
- Based on `D`:
  - If `D > 0`: Two distinct real roots → print both roots.
  - If `D == 0`: One real root (repeated) → print the root.
  - If `D < 0`: No real roots → print `"No real roots exist."`.
- Use only arithmetic operators and conditionals (do **not** import `math`; use `** 0.5` for square root).

**Sample Input:** `a=1, b=-5, c=6`
**Sample Output:**
```
Discriminant: 1.0
Root 1: 3.0
Root 2: 2.0
```

---

### Q3. 🌀 Pattern Printer — Right-Angle Number Triangle

Write a program that accepts a positive integer `N` from the user and prints the following right-angle number triangle pattern using **nested for loops**:

**Sample Input:** `N = 5`
**Sample Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Additionally, below the triangle, print the **sum of all numbers** that appear in the entire triangle.

**Sample Output (continued):**
```
Sum of all numbers in the triangle: 35
```

> **Hint:** The sum of all numbers in row `i` is `i*(i+1)/2`.

---

### Q4. 🔄 Number Classification Machine

Write a program that accepts **5 numbers** from the user one by one (using a `for` loop + `input()`) and, for each number, classifies it as:

- **Prime**: Greater than 1, divisible only by 1 and itself.
- **Perfect**: A number where the sum of its proper divisors equals itself (e.g., 6 = 1+2+3, 28 = 1+2+4+7+14).
- **Armstrong**: A number where the sum of each digit raised to the power of the number of digits equals itself (e.g., 153 = 1³+5³+3³).
- **Neither**: If it does not satisfy any of the above.

A number may belong to multiple categories simultaneously (e.g., print both Prime and Armstrong if applicable).

**Sample Output (for input 153):**
```
153 → Armstrong Number
```

**Sample Output (for input 7):**
```
7 → Prime Number
```

---

### Q5. 🏧 ATM Simulator

Simulate a simple ATM machine using a `while True` loop.

- Set an initial account balance of `₹10,000`.
- Set a PIN of `1234` (hardcoded).
- The program should:
  1. Ask the user to enter their PIN. Allow a maximum of **3 attempts**. If all fail, print `"Card blocked!"` and exit.
  2. Once authenticated, display a menu:
     ```
     1. Check Balance
     2. Deposit
     3. Withdraw
     4. Exit
     ```
  3. Allow multiple transactions until the user selects **Exit**.
  4. For **Withdraw**: Ensure the amount does not exceed the current balance. If it does, print `"Insufficient funds."`.
  5. Use `break` to exit the main loop when the user selects Exit.

---

## 📅 DAY 2 — Strings & Tuples

> **Topics Tested**: String indexing, slicing, formatting (f-strings, .format(), %), built-in string methods
> (`.upper()`, `.lower()`, `.split()`, `.join()`, `.strip()`, `.find()`, `.replace()`, `.startswith()`, `.endswith()`),
> string concatenation & repetition, Tuple creation, immutability, packing/unpacking, slicing

---

### Q6. 📊 String Statistics Dashboard

Write a program that accepts a sentence from the user and prints a formatted statistics dashboard.

The dashboard must report:
1. Total characters (including spaces/punctuation).
2. Total characters (excluding spaces).
3. Number of words.
4. Number of unique characters (case-insensitive).
5. Most frequently occurring character (ignoring spaces, case-insensitive).
6. Whether the sentence is a palindrome (True/False), ignoring spaces and case.

**Sample Input:** `"A man a plan a canal Panama"`
**Sample Output:**
```
============================================
         STRING STATISTICS DASHBOARD        
============================================
Sentence            : A man a plan a canal Panama
Total Characters    : 27
Chars (no spaces)   : 21
Word Count          : 7
Unique Characters   : 8
Most Frequent Char  : a (10 times)
Is Palindrome?      : True
============================================
```

> **Note**: Use only built-in string methods. Do **not** import any module.

---

### Q7. 🔐 Enhanced Caesar Cipher

Extend the basic Caesar cipher with an encoding AND decoding feature.

- Prompt the user for a text string, a shift value (integer), and a mode: `E` for Encrypt, `D` for Decrypt.
- **Rules**:
  - Shift only alphabetic characters. Preserve case (uppercase stays uppercase, lowercase stays lowercase).
  - Leave spaces, digits, and punctuation completely unchanged.
  - For decryption, simply apply a negative shift.
  - Wrap around the alphabet (e.g., shifting `Z` by 3 → `C`).

**Sample Input:** `text="Hello, World! 123"`, `shift=13`, `mode=E`
**Sample Output:** `"Uryyb, Jbeyq! 123"`

**Sample Input (Decrypt the above):** `text="Uryyb, Jbeyq! 123"`, `shift=13`, `mode=D`
**Sample Output:** `"Hello, World! 123"`

---

### Q8. 📦 Student Record Formatter using Tuples

A student's record is stored as a **tuple** in this format:
`(roll_number, full_name, marks_obtained, total_marks, city)`

- Define a list of **5 student tuples** hardcoded in your program (use Indian names and cities).
- For each student tuple, **unpack** it and:
  1. Calculate their **percentage** (marks_obtained / total_marks * 100).
  2. Assign a **grade**: A (≥85%), B (≥70%), C (≥55%), D (≥40%), F (<40%).
  3. Extract the student's **first name** only from `full_name` using string methods.
  4. Print a formatted report card.

**Sample Output (for one student):**
```
--------------------------------------------
Roll No    : 101
Name       : Riya Sharma
First Name : Riya
City       : Pune
Marks      : 430 / 500
Percentage : 86.00%
Grade      : A
--------------------------------------------
```

---

### Q9. 🧩 Tuple-Based Student Ranking System

You have the following hardcoded tuple of student data (name, score):

```python
students = (
    ("Arjun", 88), ("Priya", 95), ("Kiran", 72),
    ("Sneha", 95), ("Rahul", 60), ("Meera", 88)
)
```

Write a program that:
1. Finds the **highest** and **lowest** scores (without using `max()` or `min()`).
2. Lists all students with the **highest** score (there may be ties).
3. Lists all students with the **lowest** score.
4. Counts how many students **passed** (score ≥ 60) and **failed** (score < 60).
5. Calculates the **class average** score.
6. Prints a final **ranking** of all students from rank 1 (highest) to last.

> **Constraint**: Do **not** use `sorted()`, `max()`, or `min()`. Write your own logic using loops and conditionals.

---

### Q10. 🌐 URL Parser and Validator

Write a program that takes a URL string as input and extracts/validates its components.

**Rules:**
- A valid URL must start with `http://` or `https://`.
- Extract and print:
  - **Protocol** (http or https)
  - **Domain** (the part between `://` and the next `/`, or end of string)
  - **Path** (everything after the domain, or `/` if none)
  - **Subdomain check**: Does the domain start with `www.`? (True/False)
- If the URL doesn't start with `http://` or `https://`, print `"Invalid URL format."`

**Sample Input:** `"https://www.cdac.in/index.aspx?id=pg_et_sapd_CS_ai"`
**Sample Output:**
```
Protocol   : https
Domain     : www.cdac.in
Path       : /index.aspx?id=pg_et_sapd_CS_ai
Subdomain  : True (www)
```

> Use only string methods: `.startswith()`, `.find()`, slicing, `.split()`. No `import` statements.

---

## 📅 DAY 3 — Lists

> **Topics Tested**: List creation, indexing, slicing, `append()`, `insert()`, `remove()`, `pop()`, `extend()`,
> `index()`, `count()`, `sort()`, `reverse()`, list comprehension, nested lists, `in` / `not in` operators

---

### Q11. 🛒 Shopping Cart Manager

Build a console-based shopping cart application using a **list of lists**. Each item in the cart is represented as:
`[item_name, quantity, unit_price]`

Start with an empty cart `[]`.

The program must loop with a menu:
```
1. Add item
2. Remove item (by name)
3. Update quantity (by name)
4. View cart
5. Calculate total bill
6. Exit
```

**Requirements:**
- If an item being added already exists in the cart, **increase the quantity** instead of adding a duplicate.
- For **View cart** and **Total bill**, use f-string formatting to display a neat tabular receipt.
- Removing a non-existent item must print `"Item not found in cart."`.

**Sample Receipt Output:**
```
==============================================
              🛒 YOUR SHOPPING CART           
==============================================
  Item          Qty    Price    Subtotal
----------------------------------------------
  Apple          3    ₹40.00   ₹120.00
  Milk           2    ₹55.00   ₹110.00
----------------------------------------------
  TOTAL                        ₹230.00
==============================================
```

---

### Q12. 🔢 Matrix Operations with Nested Lists

Represent a **3×3 matrix** as a nested list (list of lists). Write a program that:

1. Prompts the user to enter 9 integers (row by row) to fill the matrix.
2. Displays the matrix in a formatted grid.
3. Calculates and prints:
   - The **sum of the main diagonal** (top-left to bottom-right).
   - The **sum of the anti-diagonal** (top-right to bottom-left).
   - The **row-wise sums** (sum of each row).
   - The **column-wise sums** (sum of each column).
   - The **transpose** of the matrix (rows become columns).

**Sample Output:**
```
Matrix:
 1   2   3
 4   5   6
 7   8   9

Main Diagonal Sum    : 15
Anti-Diagonal Sum    : 15
Row Sums             : [6, 15, 24]
Column Sums          : [12, 15, 18]

Transpose:
 1   4   7
 2   5   8
 3   6   9
```

---

### Q13. 📚 Student Score Analyser using List Comprehensions

You are given the following hardcoded data:

```python
students = [
    ["Ananya", [78, 85, 92, 88, 70]],
    ["Bharat", [55, 60, 45, 70, 50]],
    ["Chitra", [90, 95, 88, 92, 97]],
    ["Dev",    [40, 35, 55, 60, 50]],
    ["Esha",   [70, 75, 80, 65, 85]],
]
```

Each inner list contains a student's name and a list of scores for 5 subjects.

Using **list comprehensions** wherever possible, write a program that:
1. Computes the **average score** for each student.
2. Identifies students who **passed all subjects** (all scores ≥ 50).
3. Identifies students who **failed at least one subject** (any score < 50).
4. Finds the student with the **highest average**.
5. Prints the **subject-wise averages** (average score across all students for each subject).

> **Constraint**: Use list comprehensions for at least items 1, 2, and 3.

---

### Q14. 🎯 Word Frequency Analyser (Without Dictionaries)

Write a program that accepts a paragraph of text from the user and performs word frequency analysis **using only lists** (no dictionaries, no sets).

The program must:
1. Clean the input: convert to lowercase, remove punctuation (`.`, `,`, `!`, `?`, `;`, `:`).
2. Split into words.
3. Build two parallel lists: `words_found` and `word_counts`, where `word_counts[i]` is the number of times `words_found[i]` appears.
4. Sort both lists together so they are sorted by count in **descending order** (no `sorted()` built-in).
5. Print the **top 5** most frequent words and their counts.

**Sample Input:** `"To be or not to be that is the question to be"`
**Sample Output:**
```
Top 5 Most Frequent Words:
  1. to     → 3 times
  2. be     → 3 times
  3. or     → 1 time
  4. not    → 1 time
  5. that   → 1 time
```

> **Constraint**: Do **not** use `dict`, `set`, `Counter`, or `sorted()`.

---

### Q15. 🃏 Card Deck Simulator

Simulate a deck of playing cards using lists.

1. Create a full deck of 52 cards as a list. Each card is a string like `"Ace of Spades"`, `"7 of Hearts"`, etc.
   - Suits: `Spades, Hearts, Diamonds, Clubs`
   - Ranks: `Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King`
   - Use **list comprehension** to generate the deck.
2. **Shuffle** the deck: Write your own shuffle by swapping elements using a loop and `random.randint()`. (You may import only `random`).
3. **Deal**: Ask the user how many players (2–5) and how many cards per player (1–7). Deal cards from the top of the deck (pop from the front using list operations).
4. Display each player's hand in a formatted way.
5. Display how many cards remain in the deck.

**Sample Output:**
```
Dealing 5 cards to 3 players...

Player 1's Hand: King of Hearts, 3 of Diamonds, Ace of Clubs, 7 of Spades, 10 of Hearts
Player 2's Hand: 9 of Clubs, Queen of Diamonds, 2 of Spades, 6 of Hearts, Jack of Clubs
Player 3's Hand: 5 of Diamonds, 8 of Hearts, 4 of Clubs, King of Spades, 2 of Hearts

Cards remaining in deck: 37
```

---

## 📅 DAY 4 — Dictionaries & Exception Handling

> **Topics Tested**: Dict creation (`{}`, `dict()`), accessing values (`[]`, `.get()`), adding/updating keys,
> `.keys()`, `.values()`, `.items()`, `.pop()`, `.popitem()`, `.update()`, dict comprehension,
> `try-except-else-finally`, multiple exception types (`ValueError`, `KeyError`, `ZeroDivisionError`, `IndexError`),
> custom error messages

---

### Q16. 📇 Student Contact Book (Dictionary CRUD App)

Build a command-line **Contact Book** application where each contact is a **dictionary** with the following keys:
`name`, `phone`, `email`, `city`

The program stores all contacts in a **list of dictionaries** and must support a menu:

```
1. Add Contact
2. Search Contact (by name)
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
```

**Requirements:**
- Wrap all user input parsing (especially `int`/`float` conversions) in **try-except** blocks.
- If a contact is not found during search/update/delete, raise and handle a `KeyError`-like scenario with a friendly message.
- For **View All Contacts**, print a formatted table using f-strings.
- Before deleting, confirm with the user: `"Are you sure? (yes/no):"`.

**Sample View Output:**
```
=======================================================
  Name              Phone         Email        City
-------------------------------------------------------
  Priya Sharma      9876543210    priya@e.com  Mumbai
  Arjun Mehta       9123456789    arjun@e.com  Delhi
=======================================================
```

---

### Q17. 🏪 Inventory Management System

Create an inventory management system for a small shop using a **dictionary of dictionaries**.

The outer dictionary uses the **product name** as the key. Each value is a dictionary:
`{"quantity": int, "price": float, "category": str}`

Pre-load 5 products. Then display a menu:
```
1. View Inventory
2. Add / Restock a Product
3. Sell a Product (reduce quantity)
4. Remove a Product
5. View Products by Category
6. Calculate Total Inventory Value
7. Exit
```

**Requirements:**
- **Sell a Product**: Check stock before selling. If quantity goes to 0, remove the product from the inventory automatically and print `"[ProductName] is now out of stock and has been removed."`.
- **Total Inventory Value**: Use a **dict comprehension** to calculate the value per category and print it.
- All numeric input must be inside **try-except** blocks.

---

### Q18. 🧮 Safe Calculator with Full Exception Handling

Build a calculator that handles ALL possible runtime errors gracefully.

- Prompt the user to enter an expression as a string in the format: `num1 operator num2`
  - Example: `"15 / 0"`, `"abc + 5"`, `"10 ** 3"`, `"25 % 4"`
- Supported operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Parse the string, and use **separate except blocks** for each of the following errors:
  - `ValueError`: Non-numeric operand entered.
  - `ZeroDivisionError`: Division or modulo by zero.
  - `IndexError`: Expression doesn't have enough parts (malformed input).
  - `KeyError`: Unsupported operator entered.
  - `Exception` (generic fallback): Any other unforeseen error.
- Use a **`finally` block** to always print: `"Calculation attempt completed."`
- Loop and continue asking for input until the user types `"exit"`.

**Sample Interactions:**
```
Enter expression (or 'exit'): 10 / 0
Error: Cannot divide by zero!
Calculation attempt completed.

Enter expression (or 'exit'): hello + 5
Error: Operands must be valid numbers!
Calculation attempt completed.

Enter expression (or 'exit'): 15 ** 2
Result: 225.0
Calculation attempt completed.
```

---

### Q19. 📊 Word Frequency Counter using Dictionaries

Write a program that reads a hardcoded paragraph of text (at least 50 words, about Python or AI) and:

1. Cleans the text: lowercases everything, removes punctuation.
2. Builds a **word frequency dictionary** `{word: count}` using a loop (no `Counter`).
3. Uses **dict comprehension** to create a filtered dictionary containing only words that appear **more than once**.
4. Sorts the items by frequency (descending) and prints the top 10.
5. Prints the **total unique words** in the text.
6. Prints the **longest word** in the text.
7. Uses `.get()` method to safely look up any word the user enters and report its frequency.

**Sample Output (partial):**
```
Top 10 Most Frequent Words:
  1. python      → 8 times
  2. data        → 6 times
  3. learning    → 5 times
  ...

Total unique words : 42
Longest word       : "classification"

Enter a word to look up (or 'exit'): neural
"neural" appears 3 times.
```

---

### Q20. 🎓 Student Grade Book — Complete System

Build a **comprehensive grade book** system using a dictionary where each student's roll number maps to their data:

```python
grade_book = {
    "101": {"name": "Ananya Iyer",   "scores": {"Python": 88, "Math": 92, "AI": 85}},
    "102": {"name": "Bharat Nair",   "scores": {"Python": 55, "Math": 60, "AI": 70}},
    "103": {"name": "Chitra Menon",  "scores": {"Python": 95, "Math": 98, "AI": 92}},
    "104": {"name": "Dev Patil",     "scores": {"Python": 40, "Math": 35, "AI": 50}},
    "105": {"name": "Esha Reddy",    "scores": {"Python": 78, "Math": 82, "AI": 75}},
}
```

Write a program that provides the following analysis **without any imports**:

1. **Student Summary**: For each student, print their average score and overall grade (A/B/C/D/F).
2. **Subject Toppers**: Using dict comprehension, find the student who scored highest in each subject.
3. **Class Ranker**: Print students ranked from 1st to last based on their average score.
4. **Fail Alert**: List all students who scored below 50 in **any** subject, and which subject(s) they failed.
5. **Interactive Lookup**: Wrap in a loop — ask the user for a roll number, use `.get()` to find the student, display their full report card. Handle invalid roll numbers gracefully with `try-except`.

**Sample Report Card Output:**
```
========================================
        📋 STUDENT REPORT CARD          
========================================
Roll No    : 103
Name       : Chitra Menon
Python     : 95 / 100
Math       : 98 / 100
AI         : 92 / 100
Average    : 95.00%
Grade      : A
Rank       : 1 / 5
========================================
```

---

## 📝 Submission Guidelines

| Day   | Questions | Topic Focus                        |
|-------|-----------|------------------------------------|
| Day 1 | Q1 – Q5   | Variables, Operators, Loops, Conditionals |
| Day 2 | Q6 – Q10  | Strings & Tuples                   |
| Day 3 | Q11 – Q15 | Lists & List Comprehensions        |
| Day 4 | Q16 – Q20 | Dictionaries & Exception Handling  |

- Name your files: `Day01_Q1.py`, `Day01_Q2.py`, ... `Day04_Q5.py`
- Test each program with **at least 3 different inputs** including edge cases.
- Add a **docstring** at the top of each file explaining what the program does.

---

*Prepared for CDAC AI — Python Module 1 | Bengaluru Campus | August 2026*
