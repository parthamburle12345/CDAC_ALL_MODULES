import sys

print("adding numbers...")
args = sys.argv[1:]
print(f"the command line arguments are: {args}")
args = [int(arg) for arg in args if arg.isnumeric()]
print(f"{args=}")
total = sum(args)
print(f"{total=}")