# Normal
def dec1(func1):                        # ..... (1)
    def nowexec1():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec1


def who_is_harry1():
    print("Harry is a good boy")

abcd1 = dec1(who_is_harry1)                   #....(1)no function ta abcd1 = nowexec1  kore diloo

abcd1()                               # abcd1() mane  nowexec1()  

# Output:> 
    # Executing now
    # Harry is a good boy
    # Executed
  
print("_________________________________________________________________________")
# decorator 
def dec2(func2):
    def nowexec2():
        print("Executing now")
        func2()
        print("Executed")
    return nowexec2

@dec2
def who_is_harry2():
    print("Harry is a good boy")

# abcd2 = dec2(who_is_harry2)

who_is_harry2()

# Output:> 
    # Executing now
    # Harry is a good boy
    # Executed