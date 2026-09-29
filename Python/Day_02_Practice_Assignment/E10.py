"""
Run-Length String Compression
Write a program that prompts the user to enter a text string and compresses it using run-length encoding (listing character counts next to each repeated character). If the compressed string is not smaller in size than the original string, print the original string.

Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"
Sample Input: "abcd"
Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")
"""
text = input("Enter a string: ")

result = ""
count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1
    
    else:
        result = result + text[i] + str(count)
        count = 1

# Add the last character/group
result = result + text[-1] + str(count)

# Print compressed only if it is smaller
if len(result) < len(text):
    print(result)
else:
    print(text)
   
