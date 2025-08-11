
import random
# import math

# min_value = 1
# max_value = 6

# Refactoring: The act of change the structure of the code with out changing its meaning(functionality)
def roll_dice():
    while True:
        command = input("Roll the dice?[y/n]: ").upper()
        if command == 'Y':
            # dice_1 = math.floor(random.random()*(max_value - min_value + 1) + min_value)
            # dice_2 = math.floor(random.random()*(max_value - min_value + 1) + min_value)
            dice_1 = random.randint(1,6)
            dice_2 = random.randint(1,6)
            print(F"{dice_1, dice_2}")
        
        elif command == "N":
            print("Thank you for playing!!")
            break
        else:
            print("Invalid Choice!!")
    
roll_dice()