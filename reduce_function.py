
from functools import reduce

products = [
    {"id":1,"price":10},
    {"id":2,"price":20},
    {"id":4,"price":30.1},
]

total_price = 0
for product in products:
    total_price += product['price']
    
# print(f"Total Price: ${total_price}")

# sum = reduce(lambda x, y: x+y,[1,2,3,4],10)
# print(sum)


# prices = list(map(lambda product: product['price'],products))
# print(prices)
# total_price = reduce(lambda acc, cur: acc + cur,prices)
# total_price = reduce(lambda acc, cur: acc + cur,list(map(lambda product: product['price'],products)))
# print(total_price)


def reducer(function,iterable,initializer=None):
    itr = iter(iterable)
    acc = next(itr) if initializer is None else initializer
    for cur in itr:
        acc = function(acc,cur)
    return acc

result = reducer(lambda acc, cur: acc + cur,list(map(lambda product: product['price'],products)))
print(result)

print(next(iter([1,2,3])))