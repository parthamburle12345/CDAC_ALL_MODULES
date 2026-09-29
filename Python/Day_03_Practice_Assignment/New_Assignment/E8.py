"""
De-duplicating Shopping Cart
Scenario: An online shopping cart has duplicate items due to double-clicks: ["apple", "banana",
"apple", "orange", "banana", "banana"]. Write a program that processes the list and removes all duplicate items, 
but keeps the first occurrence of each item in its original order. Print the cleaned cart.
Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange'

"""
# # items=["apple", "banana", "apple", "orange", "banana", "banana"]
# items=input("enter a items with comma seperated:")
# clean=[]
# for i in items:
#     if i not in clean:
#         clean.append(i)
# print(clean)



items_input = input("Enter items separated by commas: ")
items = items_input.split(",")

clean = []
for i in items:
    i = i.strip()  # Removes extra spaces around words
    if i not in clean:
        clean.append(i)

print(clean)