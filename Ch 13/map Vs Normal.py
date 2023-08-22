# Map
# Map Syntax: list(map(function, list))
def square(num):
    return num*num                # num =___(1) ar vitor ar jinis gulo ak ak kore asbe.

l = [1, 2, 4]                     #_______(1)

print(list(map(square, l)))       # Important Line.. # ai l a,____(1) ar jinis gulo ak ak kore asbe.
#Output:> [1, 4, 16]

print("_______________________________________________________________________________")
# Normal 
def square(num):
    return num*num

l = [1, 2, 4]

l2 = []                                      # Important Line 

for item in l:
    l2.append(square(item))
    
print(l2)       #Output:> [1, 4, 16]

