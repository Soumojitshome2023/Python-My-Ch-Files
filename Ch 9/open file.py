with open("soumojit.txt") as f:
    a = f.read()

print(a)

# Output:> 
# Hey 
# My name is Soumojit
# I'm 18 years old

print("Line 1___________________________________________________")
#other process ...(1)
f = open("soumojit.txt")
content = f.read()
print(content)
f.close()

# Output:> 
# Hey 
# My name is Soumojit
# I'm 18 years old

print("Line 2___________________________________________________")
#other process...(2)  
f = open("soumojit.txt", "r")       # ...(1) no process ar moto same output debe
content = f.read()
print(content)
f.close()

print("Line 3___________________________________________________")
#other process.....(3)
f = open("soumojit.txt", "rb")      # binary te read korbe  
content = f.read()
print(content)
f.close()
#output:> b"Hey \r\nMy name is Soumojit\r\nI'm 18 years old"

print("Line 4___________________________________________________")
#other process...(4)  
f = open("soumojit.txt", "r") 
content = f.read(3)         #first 3 te letter k read korbe
print(content)
f.close()
#Output:> Hey               first 3 te letter k read korbe

