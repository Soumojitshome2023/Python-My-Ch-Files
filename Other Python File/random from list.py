import random

lst = ["a", "b", "c", "d", "e"]
choice = random.choice(lst)
print(choice)
#Output:>  lst ar j kono akta 

l1 = [1, 8, 7, 2, 21, 15]
random.shuffle(l1)
print(l1)

l2 = [1, 8, 7, 2, 21, 15]
print(random.sample(l2, 3))

