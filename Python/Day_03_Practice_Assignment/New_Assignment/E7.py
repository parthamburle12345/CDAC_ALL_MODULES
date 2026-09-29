"""
Treasure Map Coordinate Filter
Scenario: You have a list of coordinate pairs representing suspected treasure locations on a map:
coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]. However, the treasure can only
exist in the first quadrant of the map (where both the X coordinate and Y coordinate are strictly greater
than zero (i.e., x > 0 and y > 0)). Write a program that uses a list comprehension to filter the list and
print only the valid coordinates.
Hardcoded Input: coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
Sample Output: [[12, 5], [15, 9]]


"""


# coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]

# # List comprehension filtering for first quadrant coordinates (x > 0 and y > 0)
# valid_coords = [point for point in coords if point[0] > 0 and point[1] > 0]

# print(valid_coords)



coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]

valid_coords = []
for i in coords:
    if i[0] > 0 and i[1] > 0:
        valid_coords.append(i)

print(valid_coords)