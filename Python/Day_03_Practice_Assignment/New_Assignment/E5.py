"""
The Spy's Word Reverser
Scenario: A secret agent wants to send an encrypted message. The encryption rule is simple: reverse
every word in the sentence, but keep the order of words unchanged. Write a program that prompts
the user for a sentence, splits it, uses a list comprehension to reverse the letters of each word, and joins
them back together.
Sample Input: "Meet me at midnight"
Sample Output: "teeM em ta thgindim"

"""

message=input("enter a message :")

words=message.split()   # split the string

reversed_word=[]
for i in words:          #
    reversed_word.append(i[::-1])    #reverse the string
result = " ".join(reversed_word)     #joining the reverse string with space
print(result)



message = input("enter a message : ")

reversed_words = [word[::-1] for word in message.split()]
result = " ".join(reversed_words)

print(result)