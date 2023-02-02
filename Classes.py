# OOP

# One of the most important things going forward in terms of programming.
# Everything is OOP is an object and objects are modeled against real-world objects.
# We can make templates of an object that have defined attributes(variables) for that object, or things that they can do (behaviours = methods(functions)).

# Classes are the templates we use to create objects.
# Classes are a way of bringing both the data and functionality of our program/code together.

# Creating a class

class Dog:# creates a class; names written in snake method

    animal_kind = "canine" # class variable(attribute)

    def bark(self): # method(when functions are built within a class, they become a method). # If we remove the self from the function, but still use it below, python will not know to refer to the class and search for the variable within that class.
        #print(self.animal_kind) # Python does not know where to look for it (if it said only animal_kind). so, by putting self.animal_kind, we tell python where to look. in what class to look depending on the function and what class is the function assigned to.
        return "Woof!"
# (self) as parameter of function = I am referring to the current class. so, the bark function refers to the class dog.
# We use self because we need to refer to the class where we created the function.

# print(Dog.animal_kind) # will print the variable value, in this case "canine"
# print(Dog.bark())#Error, because we have not created an object, only the class(template).

# Instantiation of a class (Making/Creating an object from a class)

fido = Dog()
lassie = Dog()

print(type(fido)) # prints <class '__main__.Dog'> = __main__ refers to the fact that Python understands that the object has been created in the same place as the template.
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())

# Basically, we cannot use the class if we do not have objects to apply the attributes and functionality to.

#fido.animal_kind = "Big Dog" # I am talking about the object fido, but I don`t want him to be a canine anymore, but to Big Dog. And the fast that I change it in this way, I only change the attribute for fido! it does not overwrite the attribute for lassie.
print(fido.animal_kind) # changes the attribute of fido
print(lassie.animal_kind) # keeps the attribute for lassie as the one we set in the class.
Dog.animal_kind = "Dolphin" # In this instance, we change the attribute of the class, and therefore, the attributes for every object created from this template.
print(fido.animal_kind) # Fido will still come as Big Dog, because we overwrite the template, but we don`t overwrite the objects themselves.
print(lassie.animal_kind) # Now prints Dolphin, because we did not overwrite the object itself, and this object is copying the template.

# The Dog`s can still access the method!
# We can overwrite the object in terms of some aspects of the class, and that won`t make the object separate from the class.
# The variable in the class becomes an instance that is changeable for the object that has been built from the class.
