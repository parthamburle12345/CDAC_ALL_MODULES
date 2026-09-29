def main():
    name = input("What's your name? ")
    city = input("Where are you from? ")

    if name.strip() == "":
        name = "friend"

    if len(city.strip()) == 0:
        city = "your city"

    print(f"Hello {name}, how's weather in {city}?")



main()
