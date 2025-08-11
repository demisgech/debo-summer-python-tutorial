
# Positional arguments
def multiply(x:int,by:int = 1)->int:
    return x * by

# print(multiply(2,by=5))

# def sum(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
        

# print(sum(1,2,3,3,5))

# xx-arguments

def save_product(**product):
    print(product)
    
save_product(id=1,name="Apple",price=12.2)