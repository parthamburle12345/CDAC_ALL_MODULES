from vinutils import line

line()
class Book:
    def __init__(self):
        self.title = 'Let us C'
        self.author = 'Y Kanitkar'
        print('Book object instantiated!')


def main():
    b1 = Book()
    b2 = Book()
    # print(f'{id(b1) = }')
    # print(f'{type(b1) = }')
    # print(f'{dir(b1) = }')
    print(b1.title, b1.author, sep=", ")
    print(b2.title, b2.author, sep=", ")


main()
