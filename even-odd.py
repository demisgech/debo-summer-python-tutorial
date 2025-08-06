# Even or Odd

# number = 10

# if number % 2 == 0:
#     message = "Even"
# else:
#     message = "Odd"
    
    
# Ternary operator(Conditional Operator)

# message = "Even" if number % 2 == 0 else "Odd"
# print(message)


x = int(input("X: "))
y = int(input("Y: "))
op = input("operator(+,-,*,/,//,%): ")

result = 0
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    # Exception handling
    # An Exception is an error that raise by 
    # a compiler when something goes wrong
    try:
        result = x / y
    except ZeroDivisionError as ex:
        print(ex)
elif op == "//":
    try:
        result = x // y
    except ZeroDivisionError as ex:
        print(ex)
elif op == "%":
    result = x % y
    
print(result)















