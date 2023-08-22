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

print("Line 1__________________________________________________________")
# Normal 1
class A:
    name = "Baban"

    @property
    def abc(self):
        return "Raj"
                                        # Important Line
    def pqr(self, val):
        self.xyz = val                  # Important Line

e = A()
print(e.name)       
print(e.abc)

e.pqr("Khetu")                          # Important Line

print(e.xyz)                            # Important Line

print("Line 2__________________________________________________________")
# Normal 2
class A:
    name = "Baban"

    @property
    def abc(self):
        return "Raj"
                                        # Important Line
    def pqr(self, val):
        return val                      # Important Line

e = A()
print(e.name)       
print(e.abc)

s = e.pqr("Khetu")                      # Important Line

print(s)                                # Important Line

