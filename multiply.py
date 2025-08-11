
# Default argument example in a function
# def tax_calculator(income,expense:float,tax_rate = 0.2):
#     return income * tax_rate - expense

# result = tax_calculator(100, 10,0.05)
# print(result)

# X-argument
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

result = multiply(1,2,3,4,5,6)
print(result)

# xx-argument