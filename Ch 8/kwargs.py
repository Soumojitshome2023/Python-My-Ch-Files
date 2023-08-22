def myFun(**kwargs):
	for key, value in kwargs.items():
		print(key, value)


# Driver code
myFun(first='Hey', mid='are u', last='Okay ?')
#Output:>
# first Hey
# mid are u
# last Okay ?

# The special syntax **kwargs in function definitions in python is used to pass a keyworded
