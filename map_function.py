
customers = [
    {"id":1,"points": 10},
    {"id":2,"points": 5},
    {"id":3,"points": 7},
    {"id":4,"points": 17},
]

# new_customers = list(map(
#     lambda customer: {"id": customer['id'],"points": customer['points'] + 1},
#     customers))
# print(new_customers)

# customers_with_bonus = [ {"id": customer['id'],'points': customer['points'] + 5} for customer in customers if customer['points'] < 10]
customers_with_bonus = [ {**customer,'points': customer['points'] + 5} for customer in customers if customer['points'] < 10]
print(customers_with_bonus)
# print(customers)
# customers.sort(key=lambda customer: customer['points'], reverse=True)
# customers = sorted(customers,key=lambda customer: customer['points'],reverse=True)
# print("After sorted")
# print(customers)

# points = []
# for customer in customers:
#     points.append(customer['points'])
# print(points)

# def get_point(customer):
#     return customer['points']

# points = list(map(get_point,customers))
# points = list(map(lambda customer: customer['points'],customers))
# print(points)

# items = [
#     ("Product 1",10),
#     ("Product 2",13),
#     ("Product 3",6),
#     ("Product 4",16),
# ]

# prices = []
# for item in items:
#     prices.append(item)

# prices = list(map(lambda item:item[1], items))
# print(prices)
