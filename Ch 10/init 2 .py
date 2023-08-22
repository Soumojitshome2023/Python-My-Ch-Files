class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

harry = Employee("Harry", 100, "YouTube")

print(f"The name of the employee is {harry.name}")
print(f"The salary of the employee is {harry.salary}")
print(f"The subunit of the employee is {harry.subunit}")

