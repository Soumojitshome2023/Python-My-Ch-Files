# Head Tale :
p1 = input("Player 1 Enter Your Name:> ")
p2 = input("Player 2 Enter Your Name:> ")

i1 = input( p1 + " Head or Tale:> ")
i2 = input( p2 + " Head or Tale:> ")

if i1 == i2:
    print(" Invalid Input ")

import random
a = random.randint(1, 2)
if a == 1:
    print("Coin Show Head")
else:
    print("Coin Show Tale")

if i1 == "Head" and a == 1:
    print(p1 + " Win ")
    print("!! Thanks !! ")
elif i1 == "Head" and a == 2:
    print(p2 + " Win ")
    print("!! Thanks !! ")
elif i1 == "Tale" and a == 1:
    print(p2 + " Win ")
    print("!! Thanks !! ")
elif i1 == "Tale" and a == 2:
    print(p1 + " Win ")
    print("!! Thanks !! ")
else:
    print(" Invalid Input ")
    print ("!! Opps :( !!")


