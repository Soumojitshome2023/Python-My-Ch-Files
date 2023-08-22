class Person:
    def __init__(self):
        print("Initializing Person...\n")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

class Programmer(Employee):
    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n")

e = Employee()
#Output:> Initializing Person...
#         Initializing Employee...