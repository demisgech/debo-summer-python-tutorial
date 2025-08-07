#  Multiplication of odd number
# 5 Points
def odd_product(number:int)->int:
    product = 1
    is_negative = number < 0
    number = abs(number)
    for x in range(number + 1):
        if x % 2 == 1:
            product *= x
    return -product if is_negative else product

# print(odd_product(-5))

# 5 Points
def get_top_prices(prices = []):
    prices.sort()
    top_three_prices = prices[-3:]
    total = 0
    for price in top_three_prices:
        total += price
    return total
    
prices = [12.2,13.2,10.4,30.1,44.3,5.45,45]
total = get_top_prices(prices)
print(F"Sum = {total}")

# 5 Points
def factorial(number:int)->int:
    is_negative = number < 0
    number = abs(number)
    fact = 1
    for x in range(number + 1):
        if x == 0: continue
        fact *= x
    return -fact if is_negative else fact

factorial_sum = factorial(-2) + factorial(-4)
print(F"Factorial Sum = {factorial_sum}")


# 5 Points
def get_positive_numbers(numbers:list[float])->list[float]:
    positive_numbers = []
    for x in numbers:
        if x > 0:
            positive_numbers.append(x)
    return positive_numbers

numbers = [-1,3,-3.2,4,-6,5.6,7,-8,9]
positive_numbers = get_positive_numbers(numbers)
print(positive_numbers)