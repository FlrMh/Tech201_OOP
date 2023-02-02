# Initialisation

# Initialisation = Relates to setting particular data for an instance of a class.
# When we make an object, we make it more specific.

# Instantiation = the creation of an instance of an object.

class Dog:


    def __init__(self, name, colour): # We specify that we want whoever creates an object from this template, they need to specify the name and colour.
        self.animal_kind = "canine" # mention it always with self. otherwise it will not be taken into account and not recognised as part of the class.
        self.name = name # now, we are storing the data that we want to gather, and by mentioning self. it refers to the fact that it still refers to this class.
        self.colour = colour
        self.bark()
# Initialisation protects certain attributes of the dog that we don`t want to allow to be overwritten.

    def bark(self):
        return "Woof!"
# Template


# __init__ = Initialisation

fido = Dog("Fido", "brown") # we created an instance of an object that fulfills the requests of the first function. running it without mentioning the values we asked for, it will return an error.
print(fido.name)
print(fido.colour)

# Initialising a class with class variables is good practice.It is possible to set variables but it is not advised.