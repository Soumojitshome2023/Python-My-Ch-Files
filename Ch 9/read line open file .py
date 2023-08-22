f = open("soumojit.txt", "r") 

for line in f:
    print(line)

f.close()
#output:> 
# Hey 

# My name is Soumojit

# I'm 18 years old

print("Line1 _________________________________________________________")
#readline
f = open("soumojit.txt", "r") 

print(f.readlines())    #output:> ['Hey \n', 'My name is Soumojit\n', "I'm 18 years old"]

print(f.readline())     #output:> Hey
print(f.readline())     #output:> My name is Soumojit
print(f.readline())     #output:> I'm 18 years old

f.close()