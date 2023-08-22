number = int(input("Enter Number: "))
temp = number
rev = 0

while(number>0):
    dig = number%10
    rev = rev*10 + dig 
    number = number//10 

print(f" reverse number is  {rev}")
 
if temp == rev:
   print("number is a Palindrome")

else: 
    print("number is not a Palindrome")
   
