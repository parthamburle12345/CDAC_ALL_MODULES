def main():
    age = int(input("What's you age? "))

    if age < 18:
        print(f"You cannot vote now, wait for another {18-age} years.")
    else:
        print("You can and should vote.")


main()
