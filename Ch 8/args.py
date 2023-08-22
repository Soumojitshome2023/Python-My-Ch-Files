def A(*args):
   print("name is ",args[0],"age is ", args[1], "comment", args[2])
   

A("soumojit", "18", "thank u") 
#Output:> name is  soumojit age is  18 comment thank u

#other proc:
def A(*args):
   print("name is ",args[0],"age is ", args[1], "comment", args[2])
   

lst = ["soumojit", "18", "thank u"]
A(*lst) 
#Output:> name is  soumojit age is  18 comment thank u


def sum1(*numbers):
   sum = 0
   for num in numbers:
      sum+= num
   print(sum)

sum1(10,12,13)


def sum2(*numbers):
   sum = numbers[0]+numbers[1]+numbers[2]+numbers[3]
   print(sum)

sum2(10,12,13,5)