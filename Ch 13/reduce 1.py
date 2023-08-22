from functools import reduce            # sequence a kaj korar jonno use hoi.

sum = lambda a, b: a+b

l = [1, 2, 3, 4]

val = reduce(sum, l)                    # reduce Syntax: reduce(function, list)

print(val)                              # Output:> 10. because 1+2+3+4 = 10