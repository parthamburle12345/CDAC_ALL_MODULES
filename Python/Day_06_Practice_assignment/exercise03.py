class PriceAmount:
    def __init__(self, value, currency):
        self.value = float(value)
        # Standardize currency string by converting to uppercase
        self.currency = str(currency).upper()

    def __str__(self):
        return f"{self.currency} {self.value:.2f}"

    def __repr__(self):
        return f"PriceAmount(value={self.value:.2f}, currency='{self.currency}')"

    def __add__(self, other):
        if not isinstance(other, PriceAmount) or self.currency != other.currency:
            other_curr = other.currency if isinstance(other, PriceAmount) else type(other).__name__
            raise ValueError(
                f"Cannot add price amounts with different currencies: '{self.currency}' and '{other_curr}'."
            )
        return PriceAmount(self.value + other.value, self.currency)

    def __eq__(self, other):
        if isinstance(other, PriceAmount):
            return self.currency == other.currency and self.value == other.value
        return False


# Example Walkthrough
if __name__ == "__main__":
    p1 = PriceAmount(19.99, "usd")
    p2 = PriceAmount(10.01, "USD")
    p3 = PriceAmount(15.00, "EUR")

    print(str(p1))       # Output: USD 19.99
    print(repr(p1))      # Output: PriceAmount(value=19.99, currency='USD')

    total = p1 + p2
    print(str(total))    # Output: USD 30.00

    print(p1 == PriceAmount(19.99, "USD"))  # Output: True

    try:
        bad_addition = p1 + p3
    except ValueError as e:
        print(e)  # Output: Cannot add price amounts with different currencies: 'USD' and 'EUR'.
