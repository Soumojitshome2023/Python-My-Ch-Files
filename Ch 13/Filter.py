# Filter Syntax: list(filter(function, list))

def greater_than_5(num):
    if num > 5:                     # __________(1)
        return True
    else:
        return False


l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]
print(list(filter(greater_than_5, l)))     

#Output:> [6, 7, 8, 89, 98]

#filter use korle se gulo e print hoi j gulo __(1)No k satisfied kore.


