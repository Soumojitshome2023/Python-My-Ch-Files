def abc():
    return "D"

n = abc()      #def ar name ta call korte hobe
print(n)
#Output:> D

print("Line 1_____________________________________________________")
def abc():
    print("E")

x = abc()     #def ar name ta call korte hobe
#Output:> E

print("Line 2_____________________________________________________")
def abc():
    print("F")

abc()       #def ar name ta call korte hobe
#Output:> F
