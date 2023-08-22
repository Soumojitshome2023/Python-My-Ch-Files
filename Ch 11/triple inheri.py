class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath()      #Output:> I am breathing...
# print(p.company) # throws an error

e = Employee()
e.takeBreath()      #Output:> I am an Employee so I am luckily breathing..
print(e.company)    #Output:> Honda

pr = Programmer()
pr.takeBreath()     #Output:> I am a Progarmmer so I am breathing++..
print(pr.company)   #Output:> Fiverr
print(pr.country)   #Output:> India
