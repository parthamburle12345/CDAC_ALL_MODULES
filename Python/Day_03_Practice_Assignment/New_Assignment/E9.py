"""
The Josephus Elimination Game

Scenario: A group of soldiers (numbered 1 to N) stand in a circle.
Starting from the first soldier, every K-th soldier is eliminated.
The count continues with the next remaining soldier, moving clockwise.
This process repeats until only one soldier remains.
"""

n = int(input("Enter number of soldiers: "))
k = int(input("Enter elimination interval: "))

# Create the list of soldiers
soldiers = list(range(1, n + 1))

print("Soldier circle initialized:", soldiers)

# Starting index
index = 0

# Continue until only one soldier remains
while len(soldiers) > 1:

    # Calculate which soldier should be eliminated
    index = (index + k - 1) % len(soldiers)

    # Remove that soldier
    eliminated = soldiers.pop(index)

    print(f"Eliminated soldier: {eliminated} (Remaining: {soldiers})")

# Print the last remaining soldier
print("The sole survivor is:", soldiers[0])