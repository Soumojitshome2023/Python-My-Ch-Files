class A:
    def __init__(self, num):
        self.num0 = num
    def __add__(a, b):              # a = n1  b = n2 
        return a.num0 + b.num0      # a.num0 = n1.num0 = 6
                                    # b.num0 = n2.num0 = 8 
                                    
n1 = A(6)
n2 = A(8)

print(n1+n2) 