class Circle:
    # class member; shared with all objects
    # outside the class, you may access this as Circle.pi
    pi = 3.14158

    def __init__(self, radius=1.0, color='White'):
        self.radius = radius
        self.color = color
        # self.pi = 3.14158  # unnecessary member of the object

    def print(self):
        print("======= CIRCLE =======")
        print(f'Radius = {self.radius}')
        print(f'Color  = {self.color}')
        print(f'Area   = {Circle.pi * (self.radius**2)}')
        print()


def main():
    circles = [
        Circle(),
        Circle(12.3),
        Circle(10.23, 'Red'),
        Circle(84.33, 'Yellow')
    ]

    for c in circles:
        c.print()

main()
