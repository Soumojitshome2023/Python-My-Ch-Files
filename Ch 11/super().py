class Person:
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    def takeBreath(self):
        super().takeBreath()
        print("I am a Progarmmer so I am breathing++..")

pr = Programmer()
pr.takeBreath()
#Output:> I am an Employee so I am luckily breathing..
#         I am a Progarmmer so I am breathing++..
