#__str__
class abc:
    name = "Raj"

    def __str__(self):                       # Important Line
        return "Baban"

e = abc()
print(e.name)

print(e)                                     # Important Line

print("Line 1______________________________________________________________________________________________")
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

print(A.xyz)             #output:> Raj .karon @classmethod use korechi tai class  permanently change hoa geche.
print(e.xyz)  

print("Line 2______________________________________________________________________________________________")
# @property
class abc:
    name = "Raj"

    @property                                    # Important Line
    def xyz(self):
        return "Baban"
        
e = abc()
print(e.name)

print(e.xyz)                                     # Important Line

print("Line 3______________________________________________________________________________________________")
# setter
class A: 
    name = "Baban"
    
    @property
    def abc(self):
        return "Raj"

    @abc.setter                         # Important Line
    def pqr(self, val):
        self.xyz = val                  # Important Line

e = A()
print(e.name)       
print(e.abc)

e.pqr = "Khetu"    # = val              # Important Line

print(e.xyz)                            # Important Line

print("Line 4______________________________________________________________________________________________")