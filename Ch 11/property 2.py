class abc:
    name = "Raj"

    @property
    def xyz(self):
        return "Baban"
        
e = abc()
print(e.name)
print(e.xyz)
# __________________________________________________________________

# @property & def use korle e.name ar moto e.xyz hoa jai.
# without @property & def :> 
# class abc:
#     name = "Raj"
#     xyz = "Baban"
# e = abc()
# print(e.name)
# print(e.xyz)