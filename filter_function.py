
customers = [
    {"id":1,"points": 10},
    {"id":2,"points": 5},
    {"id":3,"points": 7},
    {"id":4,"points": 17},
]


# filtered_customers = []
# for customer in customers:
#     if customer['points'] >= 10:
#         filtered_customers.append(customer)
        
# print(filtered_customers)
# List comprehension

# Pythonic and Unpythonic
# filtered_customers = [ {**customer} for customer in customers if customer['points'] >= 10]
# print(filtered_customers)


# filtered_customers = list(filter(lambda customer: customer['points'] >= 10,customers))
# print(filtered_customers)

# numbers = [1,3,2,4]

# for number in enumerate(numbers):
#     print(number)

# for (index,value) in enumerate(numbers):
#     print(index,value)