# Abstraction

# We use methods to abstract objects

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in, one breath out.")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Find a mate.")

    def move(self):
        print("Onwards and Upwards.")


# cat = Animal()
# cat.eat() # this function has been abstracted.

# E.g. when you drive a car, you don t need to know how the engine works, you just need how to drive. The same with abstraction. You do not need to know how a specific function, or method works, they just need to know how to use it in the code to achieve what they want to achieve.
