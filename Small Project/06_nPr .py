# Permutation nPr  = n!/(n-r)!

n = int(input("Enter Total Number of Terms(n): "))
r = int(input("Enter Total Number of Fav(r): "))

# n!
z = 1
for i in range(1, n+1):
    z = z*i

# (n-r)!
y = 1
for j in range(1, n-r+1):
    y = y*j


permu = z/y 

print("nPr is = " + str(permu))