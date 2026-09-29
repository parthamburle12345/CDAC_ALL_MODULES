class Animal:
    def talk(self):
        print("Animal talking...")


class Dog(Animal):
    def talk(self):
            print("bow bow...")

class Cat(Animal):
    def talk(self):
            print("Meow...")

class Tiger(Animal):
    def talk(self):
            print("Grrr...")

#--------------------------------------

def yearly_meeting(animal: Animal) -> None:
    if not isinstance(animal, Animal):
        raise TypeError('You must pass an animal object as a parameter')

    animal.talk()
    # ..
    # ..


d1 = Dog()
c1 = Cat()
t1 = Tiger()

yearly_meeting(d1)
yearly_meeting(c1)
yearly_meeting(t1)
yearly_meeting(100)