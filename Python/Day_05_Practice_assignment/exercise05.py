# 1. Define global variable at top level
AUDIT_TRANSACTION_COUNT = 0

def create_bank_account(owner_name, initial_balance):
    # Initialize local variables
    balance = float(initial_balance)
    history = [f"Account created with {balance}"]
    
    def deposit(amount):
        nonlocal balance, history
        global AUDIT_TRANSACTION_COUNT
        balance += amount
        history.append(f"deposit {amount}")
        AUDIT_TRANSACTION_COUNT += 1
    
    def withdraw(amount):
        nonlocal balance, history
        global AUDIT_TRANSACTION_COUNT
        if balance >= amount:
            balance -= amount
            history.append(f"withdraw {amount}")
            AUDIT_TRANSACTION_COUNT += 1
        else:
            raise ValueError("Insufficient balance")

    def get_statement():
        # Return tuple with a copy of history to prevent external modification
        return (owner_name, balance, history.copy())
    
    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "statement": get_statement
    }


# Example Walkthrough
# Initial State
print(AUDIT_TRANSACTION_COUNT) # Output: 0

# Create account
acc = create_bank_account("Arham", 1000.0)

# Deposit
acc["deposit"](200.0)

# Withdraw
acc["withdraw"](150.0)

# Overdraft attempt (should raise ValueError)
try:
    acc["withdraw"](2000.0)
except ValueError as e:
    print(e) # Output: Insufficient balance

# Get statement
owner, bal, txn_history = acc["statement"]()
print(owner)       # Output: Arham
print(bal)         # Output: 1050.0
print(txn_history) # Output: ['Account created with 1000.0', 'deposit 200.0', 'withdraw 150.0']

# Verify global log count
print(AUDIT_TRANSACTION_COUNT) # Output: 2