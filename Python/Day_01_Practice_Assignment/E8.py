"""
Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F

"""

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)