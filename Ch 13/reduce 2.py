from functools import reduce     

def sum(a,b):
    return a + b 

l = [1, 2, 3, 4]

val = reduce(sum, l)                    # reduce Syntax: reduce(function, list)

print(val)                              # Output:> 10. because 1+2+3+4 = 10


