time = int(input("Enter time: "))


n = input("Enter your name: ")

if time >=4 and time <12:
	print('Good Morning ' + n)
elif time >=12 and time <18:
	print('Good Afternoon ' + n)
elif time >=18 and time <20:
	print('Good Evening ' + n)
else:
	print('Good Night ' + n)