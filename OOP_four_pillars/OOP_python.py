# Polymorphism
# parent class-class where the child class(currently created) inherits from.
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("Ok, let me get the stretchy pants!")

    def constrict(self):
        print("Squeeeeezeeee!")

    def climb(self):
        print("Up we go!")

    def shed_skin(self):
        print("I`m growing out of this now!")


peter = Python()
peter.breathe() # we can use methods from the super class(main class Animal)
peter.use_tongue_to_smell()
peter.attracts_through_scent()
peter.hunt()