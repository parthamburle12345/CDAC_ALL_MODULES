"""
Email Domain Extractor
Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the @) and print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".

Sample Input: "vinod@vinod.co"
Sample Output: "vinod.co"
Sample Input: "vinod.co"
Sample Output: "Invalid Email"
"""

email = input("enter an email:")
if email.count("@") == 1:
    domain=email.split("@")[1]
    print(domain)
else:
    print("invalid domain")