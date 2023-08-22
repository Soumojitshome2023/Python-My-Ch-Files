# @classmethod
class A:
    name = "Baban"
    
    @classmethod             #class k puro change kore dai.       # Important Line
    def abc(self):
        self.xyz = "Raj"

e = A()
print(A.name)
print(e.name)

e.abc()                                                           # Important Line

print(A.xyz)             #output:> Raj .karon @classmethod use korechi tai xyz ta name ar moto hoa geche.
print(e.xyz)  

print("Line 1______________________________________________________________________________________________")
# Normal 1
class A:
    name = "Baban"

    xyz = "Raj"                                                     # Important Line
    
e = A()
print(A.name)
print(e.name)

                                                                    # Important Line
print(A.xyz)           
print(e.xyz)  

print("Line 2_____________________________________________________________________________________________")
# Normal 2
class A:
    name = "Baban"

                                                                    # Important Line
    def abc(self):
        self.xyz = "Raj"

e = A()
print(A.name)
print(e.name)

e.abc()                                                             # Important Line

# print(A.xyz)    Show erron, because A ar vitor xyz nei.           # Important Line
print(e.xyz)  
