"""
Print all non-dunder attributes of a type/object
"""

def main():
    attributes = dir(list)
    for atr in attributes:
        if not atr.startswith('_'):
            print(atr, end=", ")


print("="*80)
main()
print()