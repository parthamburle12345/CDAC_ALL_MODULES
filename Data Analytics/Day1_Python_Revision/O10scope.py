x = "sachin"

def greet():
    print("2. Inside greet",x,sep="\t:\t")

print("1. before greet",x,sep="\t:\t")
greet()
print("3. After greet",x,sep="\t:\t")
print("_" * 60)

def welcome():
    x = "ramesh"
    print("2. Inside welcome",x,sep="\t:\t")

print("1. before welcome",x,sep="\t:\t")
welcome()
print("3. After welcome",x,sep="\t:\t")
print("_" * 60)

def namaskar():
    global x
    x = "tendulkar"
    print("2. Inside namaskar",x,sep="\t:\t")

print("1. before namaskar",x,sep="\t:\t")
namaskar()
print("3. After namaskar",x,sep="\t:\t")
print("_" * 60)

g = "girl"

def lady():
    g = "stree"
    def female():
        nonlocal g
        g = "nari"
        print("3.Female ",g)
    print(f"2.before female g = {g}")
    female()
    print(f"4.after female g = {g}")


print(f"1. before lady g = {g}")
lady()
print(f"5.after lady g = {g}")