

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(4)
# print(result)


def say_hello(func):
    def wrapper():
        print(F"Hello")
        func()
    return wrapper


@say_hello
def display_message():
    print("message")
    
display_message()
# def product(x,y):
#     return x * y

# def calculate(function,x,y):
#     return function(x,y)

# # result = calculate(lambda x,y: x * y,4,5)
# result = calculate(product,4,5)

# print(result)

def multiply(func):
    def wrapper(x,y):
        result = func(x,y)
        return  result * 10
    return wrapper


@multiply
def add(x,y):
    return x + y

print(add(2,3))
# def sum(function,x,y):
#     return function(x,y)+ x+ y

# result = sum(,1,2)