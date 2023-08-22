myDict = {
   "pankha": "fan",
   "Dubba" : "Box",
   "Vastu" : "Item",}

myDict["gari"] = "car"  

myDict["chand"] = "moon"

print(myDict)
#Output :> {'pankha': 'fan', 'Dubba': 'Box', 'Vastu': 'Item', 'gari': 'car', 'chand': 'moon'}

del myDict["chand"]

print(myDict)
#Output :> {'pankha': 'fan', 'Dubba': 'Box', 'Vastu': 'Item', 'gari': 'car'}
