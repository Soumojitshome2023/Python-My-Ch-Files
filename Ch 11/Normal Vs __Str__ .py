#Normal
class abc:
    name = "Raj"

    def xyz(self):                           # Important Line
        return "Baban"
        
e = abc()
print(e.name)

k = e.xyz()                                  # Important Line
print(k)       

print("______________________________________________________________________")
#__str__
class abc:
    name = "Raj"

    def __str__(self):                       # Important Line
        return "Baban"

e = abc()
print(e.name)

print(e)                                     # Important Line
