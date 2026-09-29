def main():
    name = input("What's your name? ")
    city = input("Where are you from? ")

    print(f"Hello {name}, how's weather in {city}?")

    age = int(input("How old are you? "))
    print(f"OK, so you are {age} years old!")
    future_age = age + 10
    print(f"After 10 years you will be {future_age} years old.")


main()
