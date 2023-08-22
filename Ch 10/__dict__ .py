class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

foo = MyClass(2)
bar = MyClass(3)

print(MyClass.__dict__) 
print(foo.__dict__)   #Output:>  {'i_var': 2}
print(bar.__dict__)   #Output:>  {'i_var': 3}