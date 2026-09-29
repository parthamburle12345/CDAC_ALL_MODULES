"""Vowel & Consonant Frequency
Write a program that prompts the user to enter a string and counts:

The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
The total count of all consonants.
Sample Input: "Vinod Kumar Kayartaya"

Vowel Frequencies:
a: 4
e: 0
i: 1
o: 1
u: 1
Total Consonants: 12


"""


string=input("enter a string:")
a=0
e=0
i=0
o=0
u=0
Consonants=0

for ch in string.lower():
    if ch == 'a':
        a+=1
    elif ch == "e":
        e += 1
    elif ch == "i":
        i += 1
    elif ch == "o":
        o += 1
    elif ch == "u":
        u += 1    
    elif ch.isalpha():
        Consonants +=1  
print("Vowel Frequencies:")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)

print("Total Consonants:", Consonants)        