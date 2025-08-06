# match and case

x = float(input("X: "))
y = float(input("Y: "))
op = input("Operator(+,-,*): ")

# if op == "*":
#    print(F"Product: {x * y}")
# elif op == "+":
#    print(F"Sum: {x + y}")
# elif op == "-":
#    print(F"Difference: {x - y}")
# else:
#     print("Invalid operator")


match op:
    case "*":
        print(F"Product: {x * y}")
    case "+":
        print(F"Sum: {x + y}")
    case "-":
        print(F"Diffrence: {x - y}")
    case _:
        print("Invalid Operator!") 
        
        


        