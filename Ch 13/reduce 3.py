from functools import reduce     

def mult(a,b):
    return a * b 

l = [1, 2, 3, 4]

val = reduce(mult, l)                    # reduce Syntax: reduce(function, list)

print(val)                              # Output:> 10. because 1*2*3*4 = 24


