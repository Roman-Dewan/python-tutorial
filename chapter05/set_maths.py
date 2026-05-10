value1 = {1, 2, 4, 5}
value2 = {1, 4, 6, 8, 10}

# print(value1.union(value2))
# print(value1.intersection(value2))
# # print(value1.difference(value2))
# print(value2.difference(value1))

# print(value1.symmetric_difference(value2))
# print(value1.isdisjoint(value2))

# print(value1.issubset(value2))
# print(value1.issuperset(value2))
# print(value2.issuperset(value1))
# print(value2.issubset(value1))

value1.update(value2)
print(value1)

value1.intersection_update(value2)
print(value1)

value1.difference_update(value2)
print(value1)