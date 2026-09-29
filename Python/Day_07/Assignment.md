# Day 7 Practice Assignments: File Handling, Data Formats, Serialization & Relational Databases

## Objective
Implement context-managed file operations, parse and serialize CSV and JSON structured formats, preserve object state using `pickle`, and manage relational SQLite databases using parameterized queries and ACID transactions.

---

## Easy Assignments

### Assignment 1: Structured CSV & JSON Data Processor
#### Scenario
An academic registrar stores student course registrations in a CSV file. You need to read this file, compute overall statistics, and export a summarized JSON report.

#### Problem Description
1. Create a function `process_student_records(input_csv_path, output_json_path)`:
   - Reads an `input_csv_path` containing columns: `student_id`, `name`, `course`, `score`.
   - Uses `csv.DictReader` inside a context manager to parse all rows.
   - Computes:
     - `total_students`: Total number of students processed.
     - `average_score`: Arithmetic mean of all student scores (rounded to 2 decimal places).
     - `top_scorer`: The dictionary `{"name": <name>, "score": <score>}` of the highest scoring student.
     - `course_counts`: A dictionary mapping each course name to the count of enrolled students.
   - Writes the summary dictionary into `output_json_path` formatted with an indentation of 4 spaces using `json.dump()`.

#### Example Walkthrough
```python
# Given input CSV:
# student_id,name,course,score
# 101,Arham,AI,88.5
# 102,Lisa,BDA,94.0
# 103,Vinod,AI,96.5

process_student_records("students.csv", "summary.json")

# Expected summary.json output:
# {
#     "total_students": 3,
#     "average_score": 93.0,
#     "top_scorer": {
#         "name": "Vinod",
#         "score": 96.5
#     },
#     "course_counts": {
#         "AI": 2,
#         "BDA": 1
#     }
# }
```

---

### Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)
#### Scenario
A server records raw access events as unformatted plain-text log lines. You need to parse the log lines into structured records and export them to both CSV and JSON formats.

#### Problem Description
Create a function `convert_log_file(input_log_path, output_csv_path, output_json_path)`:
1. Each line in `input_log_path` follows the format:
   `"<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>"`
   (e.g., `"2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200"`).
2. Parses each line into a dictionary containing keys: `timestamp`, `user_id`, `endpoint`, `status_code` (as integer).
3. Writes all parsed records to `output_csv_path` with a header row using `csv.DictWriter`.
4. Writes the list of records to `output_json_path` with an indentation of 2 spaces using `json.dump()`.

#### Example Walkthrough
```python
convert_log_file("server_access.log", "access_records.csv", "access_records.json")
```

---

## Medium Assignments

### Assignment 3: Object State Persistence with Pickle
#### Scenario
A machine learning experiment tracker records trained model hyperparameters and validation metrics. Researchers need to serialize experiment sessions to disk and reload them seamlessly.

#### Problem Description
1. Create a class `ExperimentSnapshot` with:
   - Attributes: `experiment_id` (str), `model_type` (str), `hyperparameters` (dict), `metrics` (dict), `timestamp` (str).
   - Method `get_best_metric(metric_name)`: Returns the numeric score for `metric_name` from `metrics`.
2. Create two helper functions:
   - `save_experiment(snapshot, file_path)`: Serializes the `ExperimentSnapshot` object to `file_path` in binary mode using `pickle.dump()`.
   - `load_experiment(file_path)`: Deserializes and returns the `ExperimentSnapshot` instance from `file_path`. If the file does not exist, raises `FileNotFoundError`.

#### Example Walkthrough
```python
exp = ExperimentSnapshot(
    experiment_id="EXP-2026-001",
    model_type="RandomForest",
    hyperparameters={"n_estimators": 100, "max_depth": 10},
    metrics={"accuracy": 0.942, "f1_score": 0.938},
    timestamp="2026-09-01 10:00:00"
)

save_experiment(exp, "experiment_01.pkl")

restored_exp = load_experiment("experiment_01.pkl")
print(restored_exp.model_type)                    # Output: RandomForest
print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942
```

---

### Assignment 4: Relational SQLite User Management System
#### Scenario
An internal employee directory stores user contact details in a SQLite database. The application must search for users, display existing details, or register new users.

#### Problem Description
Create a class `UserDatabaseManager` that connects to a SQLite database file:
1. **`__init__(self, db_path)`**: Connects to the database and creates a table `users` if it doesn't already exist:
   - Columns: `id INTEGER PRIMARY KEY AUTOINCREMENT`, `username TEXT UNIQUE NOT NULL`, `address TEXT`, `mobile TEXT`, `email TEXT`.
2. **`find_user(self, username)`**:
   - Queries the database for the given `username` using a parameterized SQL query.
   - If found, returns a dictionary: `{"id": row[0], "username": row[1], "address": row[2], "mobile": row[3], "email": row[4]}`.
   - If not found, returns `None`.
3. **`add_or_update_user(self, username, address, mobile, email)`**:
   - Checks if `username` exists.
   - If user exists, updates their `address`, `mobile`, and `email` values and returns `"UPDATED"`.
   - If user does not exist, inserts a new record and returns `"INSERTED"`.
4. **`list_all_users(self)`**: Returns a list of dictionaries for all registered users ordered alphabetically by `username`.

#### Example Walkthrough
```python
db = UserDatabaseManager("company.db")

# Insert new user
status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  # Output: INSERTED

# Search user
user_info = db.find_user("arham_k")
print(user_info["email"])  # Output: arham@cdac.in

# Update existing user
status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  # Output: UPDATED
```

---

## Hard Assignments

### Assignment 5: Transactional Banking Ledger with SQLite & ACID Rollback Management
#### Scenario
A financial transaction engine executes fund transfers between accounts in a SQLite database. The engine must support ACID guarantees: if any part of a transfer fails (e.g. insufficient funds, invalid account), the entire transaction must roll back cleanly.

#### Problem Description
Create a custom exception `TransactionError(Exception)`.
Create a class `BankingLedger` that manages an `accounts` table (`account_id TEXT PRIMARY KEY`, `holder_name TEXT`, `balance REAL`) and an `audit_log` table (`tx_id INTEGER PRIMARY KEY AUTOINCREMENT`, `from_acc TEXT`, `to_acc TEXT`, `amount REAL`, `timestamp TEXT`):
1. **`create_account(account_id, holder_name, initial_deposit)`**: Adds a new account. Raises `ValueError` if `initial_deposit < 0`.
2. **`transfer_funds(from_acc, to_acc, amount)`**:
   - Executes an atomic transfer of `amount` from `from_acc` to `to_acc`.
   - Deducts `amount` from `from_acc` and adds `amount` to `to_acc`.
   - Records an entry in the `audit_log` table.
   - **Validation & Rollback Rules**:
     - `amount` must be strictly positive (> 0).
     - Both accounts must exist in the database.
     - `from_acc` must have a sufficient balance (>= amount).
     - If any condition fails, raise `TransactionError` and execute `conn.rollback()`.
     - If all checks pass, execute `conn.commit()`.
3. **`get_balance(account_id)`**: Returns the current balance for the given account.

#### Example Walkthrough
```python
bank = BankingLedger("bank.db")
bank.create_account("ACC101", "Arham", 5000.0)
bank.create_account("ACC102", "Lisa", 2000.0)

# Valid transfer
bank.transfer_funds("ACC101", "ACC102", 1500.0)
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0

# Invalid transfer (insufficient funds) -> rolled back
try:
    bank.transfer_funds("ACC101", "ACC102", 10000.0)
except TransactionError as e:
    print(e)  # Output: Insufficient funds in account ACC101

# Balances remain untouched
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0
```
