from random import randint

class Dice():
    """Rolls a dice with varying sides decided by user input"""
    def __init__(self, sides):
        chance = sides
    
    def roll_dice(self, chance):
        x = randint(1, chance)
        print(x)

def main():
    ans = input("How many sides does the dice have? ")
    ans = int(ans)
    #Add answer to dice class
    roll = Dice(ans)
    #Call the roll method within the dice module
    roll.roll_dice(ans)

main()
        
