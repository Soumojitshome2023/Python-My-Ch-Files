s = set()

s.add(1)
s.add(2)

print(s)
#Output:> {1, 2}

s1 = s.union({2, 3, 4})

print(s1)
#Output:> {1, 2, 3, 4}           union mane 2 to set +(add) kora

s2 = s.intersection({1, 2, 3, 4})

print(s2)
#Output:> {1, 2}                  intersection mane 2 to set ar common jinis ta 