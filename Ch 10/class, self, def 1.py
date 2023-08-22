class Number:
    def sum(self):
        return self.a + self.b

num = Number()      # num = self hoa jai

num.a = 12          # self.a = num.a
num.b = 34          # self.b = num.b

s = num.sum()       # num.sum mean:> num ar vitor sum
print(s)