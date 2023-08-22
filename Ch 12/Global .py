# Global
a = 54 
def func1():
    global a                                # Important Line 
    a = 8       # Global variable
    print(f"Print statement 1: {a}")        # Output:> 8

func1()
print(f"Print statement 3: {a}")            # Output:> 8 , because akhn global variable a = 8

print("________________________________________________________________")
# Normal 
a = 54 # Global variable
def func1():
                                            # Important Line 
    a = 8   # Local variable 
    print(f"Print statement 1: {a}")        # Output:> 8
func1()
print(f"Print statement 3: {a}")            # Output:> 54 , because akhn global variable a = 54