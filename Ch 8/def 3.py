def abc():
    return "D"

n = abc()      #function call
print(n)
#Output:> D

print("Line 1_____________________________________________________")
def abc():
    print("E")

x = abc()     #function call
#Output:> E

print("Line 2_____________________________________________________")
def abc():
    print("F")

abc()       #function call
#Output:> F
