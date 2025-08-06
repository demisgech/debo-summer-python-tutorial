
# from typing import Union
def factorial(number:int)->int:
    fact = 1
    is_negative = number < 0
    number = abs(number)
    for x in range(number+1):
        if x == 0:
            continue
        fact *= x
    return -fact if is_negative else fact

def get_factorial(number:int)->int:
    if number == 0 or number == 1:
        return 1
    return number * get_factorial(number - 1)

x = int(input("Number: "))
result = get_factorial(x)
print(F"{x}! = {result}")


# for x in range(1,4):
#     if x == 2:
#         break # Terminate
#     print(F"x: {x}")
    
# for x in range(1,4):
#     if x == 2:
#         continue # Move to the next iteration
#     print(F"x: {x}")

