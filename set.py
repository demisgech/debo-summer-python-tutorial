# Set

set_a = {"A","B","C"}
# set_a.add("F")
# set_a.update({"A","B","E"})
# set_a.remove("A")
# set_a.pop()
# set_a.discard("A")
# set_a.clear()
new_set = set_a.intersection({"A","B","D"})
users = ["Abebe","Alemu","Kebede"]
print(users)
users = set(users)
print(users)
# print(new_set)


# set_b = {"C","D","B"}
# set_c = set_a.union(set_b)
# set_c = set_a.difference(set_b)
# set_c = set_b.difference(set_a)

# print(set_c)


numbers = [1,1,2,2,3,4]
numbers = list(set(numbers))
print(numbers)