from random import randint

print("6 sided:-")
# Define a class for a six-sided die
class die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        r = 0
        while r < 10:
            score = randint(1, 6)  # Generate a random number between 1 and 6
            print(score)
            r = r + 1

# Create an instance of the die class and roll the dice
ibhav = die()
ibhav.roll_dice()

print("10 sided:-")
# Define a class for a ten-sided die
class die2:
    def __init__(self, sides=10):
        self.sides = sides

    def roll_dice(self):
        r = 0
        while r < 10:
            score = randint(1, 10)  # Generate a random number between 1 and 10
            print(score)
            r = r + 1

# Create an instance of the die2 class and roll the dice
ibhav2 = die2()
ibhav2.roll_dice()

# Define a class for a twenty-sided die
class die3:
    def __init__(self, sides=20):
        self.sides = sides

    def roll_dice(self):
        r = 0
        while r < 10:
            score = randint(1, 20)  # Generate a random number between 1 and 20
            print(score)
            r = r + 1

print("20 sided:-")
# Create an instance of the die3 class and roll the dice
ibhav3 = die3()
ibhav3.roll_dice()