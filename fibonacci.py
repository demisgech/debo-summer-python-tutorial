
# 1,1,2,3,5
def fibonacci(number:int):
    return 1 if number < 2 else fibonacci(number - 2) + fibonacci(number - 1)
  

def generate_sequence(number:int)->list[int]:
    numbers = []
    for x in range(number + 1):
        numbers.append(fibonacci(x))
    return numbers

