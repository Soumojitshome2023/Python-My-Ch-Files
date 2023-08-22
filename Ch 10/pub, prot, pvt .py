class A:
    abc = "Soumojit"            # public variable
    _protec = "Raj"             # protected variable 
    __private = "Khetu"         # private variable 

e = A()

print(e.abc)           #Output:> Soumojit
print(e._protec)       #Output:> Raj
#print(e.__private)    # show error
print(e._A__private)   #Output:> Khetu     