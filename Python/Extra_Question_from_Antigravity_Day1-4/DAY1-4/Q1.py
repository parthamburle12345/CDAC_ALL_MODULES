num = int(input("Enter a positive number: "))

original = num
steps = 0

print("Original number :", original)

while num >= 10:
    digits = str(num)
    total = 0

    for d in digits:
        total += int(d)
    steps += 1
    print(f"Step {steps} : {' + '.join(digits)} = {total}")
    num = total

print("Digital Root :", num)
print("Total Steps  :", steps)

