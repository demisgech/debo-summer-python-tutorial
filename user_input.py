# Getting input for user using the input() function

# name = input("What is your name?: ")
# print(name)

# Exercise

sales = float(input("Sales: "))
print("Sales: $" + str(sales))

discount_rate = 0.1
discount = sales * discount_rate
print("Discount: $" + str(discount))

tax_rate = 0.15
tax = sales * tax_rate
print("Tax: $" + str(tax))

net_price = sales + tax - discount
print("Net Price: $" + str(net_price))

print("Hello world")