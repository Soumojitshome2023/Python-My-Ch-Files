#Max & reduce
from functools import reduce
l = [3, 8, 455, 2, 5, 45]

a = reduce(max, l)
print(a)
#Output:> 455

print("__________________________________________")
# Simple Max
l1 = [3, 8, 455, 2, 5, 45]

print(max(l1))      #Output:> 455