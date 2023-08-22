class Employee:
    salary = 100

    @classmethod                     #class k puro change kore dai
    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)  #output:> 455 .karon @classmethod use korechi tai class  permanently change hoa geche
