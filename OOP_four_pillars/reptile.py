# Inheritance

from animal import Animal # greyed out because we haven`t used it yet.

class Reptile(Animal):

    def __init__(self):
        super().__init__() # super is a key word that related back to the main class (Animal) which basically inherits all the attributes of the main class. Like russian dolls: this creates the first russian doll on top of the main one.
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles tetrapods...
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None # Placeholder


    def seek_heat(self):
        print("It`s chilly outside, where is the sun?")

    def hunt(self):
        print("Wait, wait, wait ... Pounce.")

    def use_venom(self):
        print("If I got it, I am going to use it.")

    def attracts_through_scent(self):
        print("Time to spray some eau de toilette.")

# jeremy_the_reptile = Reptile() # prints "One breath in, one breath out."
# jeremy_the_reptile.breathe()
# jeremy_the_reptile.use_venom()
