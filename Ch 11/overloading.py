class Number:
    def __init__(self, num):
        self.num0 = num

    def __add__(self, num5):
        print("Lets add")
        return self.num0 + num5.num0

n1 = Number(4)
n2 = Number(6)

print(n1 + n2)


