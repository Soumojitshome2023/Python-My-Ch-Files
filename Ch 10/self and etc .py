class Employee:
    company = "Google"

    def getSalary(self, signature, age):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature} and age is {age}")

harry = Employee()
harry.salary = 100000

harry.getSalary("Thanks!", "18")