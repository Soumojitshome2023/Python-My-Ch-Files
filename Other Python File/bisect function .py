import bisect           
number = 5

a = [1, 2, 3, 4, 6, 7, 8, 9,]

print(bisect.bisect(a, number ))
#Output:> 4   # index 4 a number 5 insert korle list ta sort thakbe
 
bisect.insort(a, number)
print(a)  #Output:> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# bisect tokhn use kora hoi jokhn kono number k, kono akta list a amon vabe 
# insert korate hobe jate list ta sort thakee. 