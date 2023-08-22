
def xyz(a, b):
    yield a
    yield b


res = xyz(5, 6)
print(res)              # Output:> <generator object xyz at 0x0000014FC9639BD0>

print(next(res))       # Output:> 5
print(next(res))       # Output:> 6

print("Line 1_______________________________________________________________________")
# yield 
def getNum (x):
    for i in range(x):
        yield i

seq = getNum (3)
print(seq)                  # Output:> <generator object getNum at 0x00000136F4D49C40>

print(seq.__next__())       # Output:> 0
print(seq.__next__())       # Output:> 1
print(seq.__next__())       # Output:> 2

print("Line 2_______________________________________________________________________")
# yield 2
def number (x):
    for i in range(x):
        yield i

abc = number (6)
print(next(abc))    #Output:> 0
print(next(abc))    #Output:> 1
print(next(abc))    #Output:> 2  

