class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

def process_order(catalog, order):
    # Validation Phase: Check all items before making any modifications
    for product_id, requested_qty in order.items():
        if product_id not in catalog:
            raise ProductNotFoundError(f"Product '{product_id}' not found in store catalog.")
        
        available_stock = catalog[product_id]["stock"]
        if requested_qty > available_stock:
            raise OutOfStockError(
                f"Product '{product_id}' is out of stock. Requested: {requested_qty}, Available: {available_stock}."
            )
    
    # Execution Phase: Only executes if all items passed validation
    total_cost = 0.0
    for product_id, requested_qty in order.items():
        catalog[product_id]["stock"] -= requested_qty
        total_cost += catalog[product_id]["price"] * requested_qty
        
    return float(total_cost)


# Example Walkthrough
catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}

# 1. Successful Order
total = process_order(catalog, {"P01": 2, "P02": 1})
print("Total Cost:", total)
# Returns: 40.0
print(f"Catalog stock changes to: P01 stock = {catalog['P01']['stock']}, P02 stock = {catalog['P02']['stock']}")
# Catalog stock changes to: P01 stock = 3, P02 stock = 9

# 2. Failed Order (Triggers Rollback)
# Current Catalog: {"P01": {"price": 10.0, "stock": 3}, "P02": {"price": 20.0, "stock": 9}}
try:
    total = process_order(catalog, {"P01": 2, "P02": 15})
except OutOfStockError as e:
    print(e)
    # Output: Product 'P02' is out of stock. Requested: 15, Available: 9.

# Verify Catalog Stock: P01 must remain at 3 (NOT decreased to 1).
print("Verified P01 stock:", catalog["P01"]["stock"])
# Output: 3
