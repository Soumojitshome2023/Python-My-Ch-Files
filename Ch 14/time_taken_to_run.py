import time
a = time.time() #its gives time from 1st january 1970

print(a)  #its gives time from 1st january 1970

i = 0
while(i<500):
    print(i)
    i = i + 1

t1 = time.time() - a

print(t1)   # time taken to run while loop