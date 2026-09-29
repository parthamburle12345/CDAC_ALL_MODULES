"""
Grading on a Curve
Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated
test scores. Convert them to a list of integers. Using a single list comprehension with conditionals,
apply the following curve rules:
If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). Print
the original and the curved grades.
Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]

"""

# scores_input = input("Enter space-separated scores: ")

# original = [int(x) for x in scores_input.split()]

# # Curve logic: add 10 if score < 50, else add 5, capping the result at 100
# curved = [min(100, x + 10) if x < 50 else min(100, x + 5) for x in original]

# print("Original:", original)
# print("Curved:", curved)



scores_input = input("Enter space-separated scores: ")

# Convert input string to a list of integers
original = []
for i in scores_input.split():
    original.append(int(i))

# Apply curve rules using a standard loop
curved = []
for j in original:
    if j < 50:
        new_score = j + 10
    else:
        new_score = j + 5

    # Cap the score at 100
    if new_score > 100:
        new_score = 100

    curved.append(new_score)

print("Original:", original)
print("Curved:", curved)