"""
Shift Cipher Encrypter
Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the string by the specified shift number down the alphabet. Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

Sample Input: (User inputs string "Vinod" and shift 3)
Sample Output: "Ylqrg"

"""


text = input("Enter a string: ")
shift = int(input("Enter shift: "))

result = ""

for i in text:
    if i.isupper():
        result += chr((ord(i) - ord('A') + shift) % 26 + ord('A'))

    elif i.islower():
        result += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))

    else:
        result += i

print(result)