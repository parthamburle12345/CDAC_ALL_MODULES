def manage_bookstore_inventory(inventory, action, book_title, quantity=0):
    action_clean = action.lower()
    if action_clean == "add":
        inventory[book_title] = inventory.get(book_title, 0) + quantity
        return inventory
    elif action_clean == "sell":
        if book_title not in inventory:
            print(f"Error: Book '{book_title}' not found in inventory.")
            return inventory
        if quantity > inventory[book_title]:
            print(f"Error: Insufficient stock for '{book_title}'. Available: {inventory[book_title]}.")
            return inventory
        inventory[book_title] -= quantity
        if inventory[book_title] == 0:
            del inventory[book_title]
        return inventory
    elif action_clean == "lookup":
        return inventory.get(book_title, 0)
    else:
        print("Invalid Action Parameter")
        return inventory

# Initial Inventory
inventory = {"Python Basics": 10, "Learning AI": 5}
print("Initial:", inventory)

# 1. Add Stock
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
print("After Add:", inventory)
# Result: {"Python Basics": 15, "Learning AI": 5}

# 2. Sell Stock Safely (Missing Book)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
# Console output: Error: Book 'Data Science 101' not found in inventory.

# 3. Sell Stock (Insufficient)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
# Console output: Error: Insufficient stock for 'Learning AI'. Available: 5.

# 4. Sell Stock (Exactly Zero Stock)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
print("After Sell (Zero Stock):", inventory)
# Result: {"Python Basics": 15}

# 5. Lookup Stock
stock_found = manage_bookstore_inventory(inventory, "lookup", "Python Basics")
print("Lookup 'Python Basics':", stock_found) # Output: 15
stock_missing = manage_bookstore_inventory(inventory, "lookup", "Unknown Book")
print("Lookup 'Unknown Book':", stock_missing) # Output: 0
