import copy
import os

class AccountNotFoundError(Exception):
    pass

class OverdraftError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

def process_transaction_batch(accounts, batch_list, log_path):
    # Atomicity: Create a deep copy of accounts to act as a restore point (backup)
    backup = copy.deepcopy(accounts)
    
    try:
        for tx in batch_list:
            acc = tx.get("acc")
            tx_type = tx.get("type")
            amt = tx.get("amt", 0)
            
            if acc not in accounts:
                raise AccountNotFoundError(f"Account '{acc}' not found.")
            
            if tx_type not in ("deposit", "withdraw"):
                raise InvalidTransactionError(f"Invalid transaction type '{tx_type}'.")
            
            if amt <= 0:
                raise InvalidTransactionError("Transaction amount must be positive.")
            
            if tx_type == "withdraw":
                if accounts[acc] < amt:
                    raise OverdraftError(
                        f"Insufficient funds. Account {acc} has balance {accounts[acc]}, requested {amt}."
                    )
                accounts[acc] -= amt
            elif tx_type == "deposit":
                accounts[acc] += amt

        # If all transactions executed successfully:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[SUCCESS] Batch completed. {len(batch_list)} transaction(s) processed.\n")
            
        return accounts

    except Exception as e:
        # Rollback: Restore accounts to backup
        accounts.clear()
        accounts.update(backup)
        
        # Log the rollback action
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[ROLLBACK] Batch aborted: {type(e).__name__} - {e}\n")
            
        # Re-raise the caught exception
        raise


# Example Walkthrough from Assignment.pdf
accounts = {"ACC01": 100.0, "ACC02": 50.0}
log_file = os.path.join(os.path.dirname(__file__), "transactions.log")

# Clean up any existing log file from prior test runs for fresh demonstration
if os.path.exists(log_file):
    os.remove(log_file)

print("Initial Accounts:", accounts)

# Batch 1: Valid transactions
batch_1 = [
    {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
    {"acc": "ACC02", "type": "deposit", "amt": 20.0}
]
accounts = process_transaction_batch(accounts, batch_1, log_file)
print("Accounts after Batch 1:", accounts)
# Result: accounts changes to {"ACC01": 70.0, "ACC02": 70.0}

# Batch 2: Invalid transaction (triggers rollback)
batch_2 = [
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0}  # Overdraft!
]

try:
    accounts = process_transaction_batch(accounts, batch_2, log_file)
except OverdraftError as e:
    print(f"Caught: {e}")

# Verify Rollback: ACC01 must remain 70.0, NOT updated to 120.0.
print("Accounts after Batch 2 Rollback:", accounts)
# Output: {"ACC01": 70.0, "ACC02": 70.0}

# Display log file content
print("\n--- transactions.log contents ---")
with open(log_file, "r", encoding="utf-8") as f:
    print(f.read(), end="")
