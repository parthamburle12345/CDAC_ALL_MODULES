class MathUtils:

    @classmethod
    def square(cls, num:int):
        # we can use the class related members here via `cls`
        return num ** 2

    @staticmethod
    def factorial(num):
        f = 1
        for i in range(1, num+1):
            f *= i
        return f

    @staticmethod
    def fibonacci(num):
        a, b = -1, 1
        for _ in range(num):
            c = a + b
            a, b = b, c
        return c

# ------------------------------
m = MathUtils()
print(f'{MathUtils.fibonacci(10) = }')
print(f'{m.factorial(5) = }')   # bad practice; avoid
print(f'{MathUtils.square(123) = }')