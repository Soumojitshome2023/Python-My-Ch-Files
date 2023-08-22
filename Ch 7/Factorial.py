num = int(input("Enter Number:" ))

z = 1
for i in range (1, num+1):
    z = z*i                     #--------(1)

print(z)
#____________________________________________________________

#(1) 4!  z = z*i                z =1 theke start and i = 1 theke 4 obdi
#        z = 1*1 = 1     
#        z = 1*2 = 2     
#        z = 2*3 = 6     
#        z = 6*4 = 24    
#  ans: 24