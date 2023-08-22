class Employee:
    salary = 5600
    salarybonus = 400
    name = "Raj"

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.name)
print(e.totalSalary)
# @property use korle e.name ar moto e.totalSalary hoa jai
