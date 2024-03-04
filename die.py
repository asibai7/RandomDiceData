from random import randint

class Die:
    #class for a single die
    def __init__(self, num_sides = 6):
        #assume a six sided die
        self.num_sides = num_sides
    
    def roll(self):
        #return a rand value between 1 and 6
        return randint(1, self.num_sides)