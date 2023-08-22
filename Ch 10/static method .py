# Normal 
class Employee:

    def greet(self):
        print("Good Morning, Sir")

harry = Employee()
harry.greet()       # Employee.greet()

print("___________________________________________________________________________")
# @staticmethod
class Employee:

    @staticmethod           # self na likhe  @staticmethod lekha jai
    def greet():
        print("Good Morning, Sir")

harry = Employee()
harry.greet()        # Employee.greet()

