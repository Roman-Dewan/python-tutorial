''' 
 List are mutable, ordered, and allow duplicate elements. They are defined using square brackets [] and can contain elements of different data types.
 Lists are commonly used to store collections of items, such as numbers, strings, or even other lists. They provide various methods for manipulating and accessing the elements within them.
 
 Tuples, on the other hand, are immutable, ordered, and also allow duplicate elements. They are defined using parentheses () and can contain elements of different data types. Once a tuple is created, its elements cannot be modified or changed. Tuples are often used to represent fixed collections of items that should not be altered, such as coordinates or RGB color values.

 '''

friends = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", 2.12, 3.14, True, False]
print(friends)
friends.append("Fig")
print(friends)

list1 = [3, 1, 5, 2, 4]
list1.sort()
print(list1)
list1.reverse()
print(list1)

list2 = [1, 3, 5, 7, 9, 2, 3, 4, 5, 6, 8]
list2.insert(2, 10)
print(list2)

list2.remove(2)
print(list2)

# list2.pop()
print(list2)

index = list2.index(7)
print(index)

list2.count(5)
print(list2)