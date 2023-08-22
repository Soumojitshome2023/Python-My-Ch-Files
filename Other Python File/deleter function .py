# Deleter
class student:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
                
    @property                           #imp line    
    def email(self):
        if(self.name == None):
            return "Member not found"
        return str(self.name) + "." + str(self.birth_year) + "@gmail.com"
        
    @email.deleter                          #imp line
    def email12(self):
        self.name = None
        self.birth_year = None

Max = student("Raj", 2004)
print(Max.email)        #output:> Raj.2004@gmail.com

del Max.email12                         #imp line
print(Max.email)        #output:> Member not found

print("_____________________________________________________________________")
# Normal
class student:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
                                            # imp line
    def email(self):
        if(self.name == None):
            return "Member not found"
        return str(self.name) + "." + str(self.birth_year) + "@gmail.com"
                                            # imp line
    def email12(self):
        self.name = None
        self.birth_year = None

Max = student("Raj", 2004)
print(Max.email())          #Output:> Raj.2004@gmail.com

Max.email12()                               # imp line       
print(Max.email())          #output:> Member not found