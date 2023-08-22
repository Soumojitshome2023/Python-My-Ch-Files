# Combination nCr = n!/r! * (n-r)!

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

# r!
w = 1
for k in range(1, r+1):
    w = w*k

comb = z/(w*y)

print("nCr is = " + str(comb))