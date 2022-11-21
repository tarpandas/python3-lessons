# Rolling two dice
import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second # returning two values return a tuple


dice = Dice()
print(dice.roll())