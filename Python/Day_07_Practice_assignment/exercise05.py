import sqlite3
import os
from datetime import datetime

# 1. Custom Exception
class TransactionError(Exception):
    pass


# 2. BankingLedger Class
class BankingLedger:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        """Creates the accounts and audit_log tables."""
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id TEXT PRIMARY KEY,
            holder_name TEXT NOT NULL,
            balance REAL NOT NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_acc TEXT NOT NULL,
            to_acc TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp TEXT NOT NULL
        );
        """)
        self.conn.commit()

    def create_account(self, account_id, holder_name, initial_deposit):
        """Creates a new bank account with initial deposit."""
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO accounts (account_id, holder_name, balance) VALUES (?, ?, ?)",
            (account_id, holder_name, float(initial_deposit))
        )
        self.conn.commit()

    def get_balance(self, account_id):
        """Returns the current balance for the given account."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        row = cursor.fetchone()
        if row is None:
            raise TransactionError(f"Account '{account_id}' does not exist.")
        return float(row[0])

    def transfer_funds(self, from_acc, to_acc, amount):
        """Atomically transfers funds from from_acc to to_acc with ACID rollback."""
        cursor = self.conn.cursor()
        
        try:
            if amount <= 0:
                raise TransactionError("Transfer amount must be positive.")

            # Validate source account existence
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_acc,))
            from_row = cursor.fetchone()
            if not from_row:
                raise TransactionError(f"Source account {from_acc} does not exist.")
            from_balance = from_row[0]

            # Validate destination account existence
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (to_acc,))
            to_row = cursor.fetchone()
            if not to_row:
                raise TransactionError(f"Destination account {to_acc} does not exist.")

            # Validate sufficient funds
            if from_balance < amount:
                raise TransactionError(f"Insufficient funds in account {from_acc}")

            # Deduct from source
            cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE account_id = ?",
                (amount, from_acc)
            )

            # Add to destination
            cursor.execute(
                "UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
                (amount, to_acc)
            )

            # Record in audit log
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO audit_log (from_acc, to_acc, amount, timestamp) VALUES (?, ?, ?, ?)",
                (from_acc, to_acc, amount, now_str)
            )

            # All operations succeeded -> commit transaction
            self.conn.commit()

        except Exception:
            # Atomic rollback on any failure
            self.conn.rollback()
            raise

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()


# Example Walkthrough
if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(__file__), "bank.db")
    if os.path.exists(db_file):
        os.remove(db_file)

    bank = BankingLedger(db_file)
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

    bank.close()
