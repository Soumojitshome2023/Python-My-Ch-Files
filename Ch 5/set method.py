# an empty set can be created uding the below syntax:
b = set()
print(type(b))

# adding values to an empty set
b.add(4)
b.add(5)
# cannot add list and dict
print(b)
print(len(b)) # print the length of this set
# remove of an item
b.remove(5)
print(b)

print(b.pop())
print(b)

