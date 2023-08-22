class Employee:
    salary = 5600
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)

e.totalSalary = 5800     # = val
print(e.salary)
print(e.salarybonus)
