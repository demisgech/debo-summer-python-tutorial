
# Dictionary

product = {
    "id": 1,
    "name": "Product Name",
    "price": 10.1
}
# print(product)
# print(type (product))
# print(product['id'])

# print(product.values())
# print(product.get("name"))
# print(product.get("age","unkown"))
# print(product.keys())
# print(product.items())

for item in product.items():
    
    print(item)
    # print(item,product[item])