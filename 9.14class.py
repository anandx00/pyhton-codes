"""-14. Dice: The module random contains functions that generate random num-
bers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times"""
import random
class die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print( random.randint(1,self.sides))
k=die()
k1=die(10)
k2=die(20)
for i in range(10):
    k.roll_die()
for i in range(10):
    k1.roll_die()
    k2.roll_die()




