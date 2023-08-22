class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"

e = Employee()
e.showDetails()     # output:> This is an employee
p = Programmer()
p.showDetails()     # output:> This is an employee
print(p.company)    # output:> Google