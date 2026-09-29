def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    # 1. Sum the base_price and all side item prices (*items) to compute raw subtotal
    raw_subtotal = base_price + sum(items)
    
    # 2. Deduct the discount from the raw subtotal to compute discounted subtotal
    discounted_subtotal = raw_subtotal * (1 - (discount / 100))
    
    # 3. Compute the tax value by multiplying discounted subtotal by tax_rate
    tax = discounted_subtotal * tax_rate
    
    # 4. Add tax and delivery_fee to discounted subtotal to get the final bill
    final_total = discounted_subtotal + tax + delivery_fee
    
    # 5. Return final total rounded to 2 decimal places
    return round(final_total, 2)


# Example Walkthrough
# 1. Standard meal, no sides, default tax, no discount, no delivery
total1 = calculate_cafeteria_bill(100.0)
print(f"Total 1: {total1:.2f}")
# Subtotal = 100.0
# Tax = 100.0 * 0.05 = 5.0
# Return: 105.00

# 2. Meal with sides, custom tax rate, 10% discount, flat delivery fee
total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
print(f"Total 2: {total2:.2f}")
# Raw Subtotal = 100.0 + (20.0 + 30.0) = 150.0
# Discounted Subtotal = 150.0 * (1 - 10/100) = 135.0
# Tax = 135.0 * 0.08 = 10.8
# Final Total = 135.0 + 10.8 + 15.0 = 160.8
# Return: 160.80
