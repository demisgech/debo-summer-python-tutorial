
# 5! = 120
# 4! = 24
# -1! = "Negative number doesn't have factorial"
# -1! = 1
# factorial = 1
# number = int(input("Number: "))
# if number < 0:
#     print("Sorry!! Number cannot be negative!")
# else:
#     for x in range(0,number + 1):
#         if x == 1 or x == 0: 
#             pass
#         else:
#             factorial *= x
#     print(F"{number}! = {factorial}")
    
# if number < 0:
#     print("Sorry!! Number cannot be negative!")
# else:
#     i = 0
#     while i <= number:
#         if i == 1 or i == 0: 
#             pass
#         else:
         
#             factorial *= i
#         i +=1
#     print(F"{number}! = {factorial}")
    
# for x in range(1,6):
#     print("*"*x)

import random
import math

max_number = 99
min_number = 10
# x =math.floor(random.random()*(max_number - min_number + 1) + min_number)
x = random.randint(min_number,max_number)
print(x)

# 