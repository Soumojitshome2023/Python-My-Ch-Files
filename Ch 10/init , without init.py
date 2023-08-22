# normal (without __init__)
class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!")      # alada kore call korte hoi..

print('______________________________________________________________________________________________')

# __init__
class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

harry = Employee("Harry", 100, "YouTube")     # alada kore call korte hoi naa..

print(f"The name of the employee is {harry.name}")
print(f"The salary of the employee is {harry.salary}")
print(f"The subunit of the employee is {harry.subunit}")

