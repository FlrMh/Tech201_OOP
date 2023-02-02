# Encapsulation
# Encapsulation = hiding thigs from the user

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        k
        self.cold_blooded = True
        self.venom = None # placeholders, as some snakes have venom and some don t
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it tastes or smells nice?")


sidney = Snake()
sidney.seek_heat()
# Encapsulation method allows us to hide form users things that they don`t need to see.
# Abstraction vs Encapsulation = abs means when i am using the methods, i do not need to kow how it works(in the same file)- so, once i wrote the function, i don`t need to know how it works, as long as it works. encaps is all about hiding it via another file.