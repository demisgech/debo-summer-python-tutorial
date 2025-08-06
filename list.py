# List

# numbers = [1,2,3,4]
# for number in  numbers:
#     print(number)
    
# prices = [12,10,34,56,71,53]
# sum = 0
# for price in prices:
#     if price % 2 == 0:
#         sum = sum + price
    
# print(F"Sum = {sum}")

# prices = [12,10,34,56,71,53]
# min_price = prices[0]    
# max_price = prices[0]

# for price in prices:
#     if min_price > price:
#         min_price = price
        
#     if max_price < price:
#         max_price = price
    
# min_max_sum = min_price + max_price
# print(F"Min Max Sum = {min_max_sum}")
    
# numbers = [1,4,3,3,2,5]
# [1,2,3,4,5]
# [5,4,3,2,1]
# numbers.append(3)
# numbers.insert(2,3)
# numbers.reverse()
# numbers.sort()
# numbers.append(5)
# numbers.sort()
# numbers.reverse()
# numbers.remove(3)
# numbers.remove(3)
# numbers.clear()
# index = numbers.index(3)
# print(index)
# print(numbers)

# numbers.pop(1)
# another_numbers = [6,7,8]
# numbers.extend(another_numbers)
# print(numbers)

numbers = [1,2,3,4,5]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# print(even_numbers)

# numbers = [1,4,3,6,7,2,8,5]
# numbers.sort()
# first_five_numbers = numbers[:5]
# # sub_numbers = numbers[-2:]
# # print(sub_numbers)
# print(first_five_numbers)

# Identity operators
# print(10 is 10)
# print("10" is not "11")

# Membership
# print("a" in "Abc")
# print("a" not in "Abc")

# numbers = [1,2,3,4]

# if 5 not in numbers:
#     print("Not found")
# else:
#     print("Found")

value = list(range(10))
result = list(range(2,21))[10::2]
print(result)