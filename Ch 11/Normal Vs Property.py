# @property
class abc:
    name = "Raj"

    @property                                    # Important Line
    def xyz(self):
        return "Baban"
        
e = abc()
print(e.name)

print(e.xyz)                                     # Important Line

print("Line 1___________________________________________________________________________")
#Normal 1
class abc:
    name = "Raj"
                                                  # Important Line
    def xyz(self):
        return "Baban"
        
e = abc()
print(e.name)

k = e.xyz()     
print(k)                                           # Important Line
#OR, print(e.xyz())

print("Line 2___________________________________________________________________________")
# Normal 2
# @property & def use korle e.name ar moto e.xyz hoa jai.
# without @property & def :> 

class abc:
    name = "Raj"

    xyz = "Baban"                                   # Important Line

e = abc()
print(e.name)

print(e.xyz)                                        # Important Line