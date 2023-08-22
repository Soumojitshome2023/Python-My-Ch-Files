class Freelancer:
    company = "Fiverr"

class Employee:
    company = "Visa"

class Programmer(Freelancer, Employee):
    name = "Raj"

p = Programmer()
print(p.name)       #Output:> Raj
print(p.company)    #Output:> Fiverr  #Freelancer first a aache tai freelancer-ar company print hobe..