name = "Harry"
channel = "CodeWithHarry"
type = "Coding"

a = "This is {} and his {} channel is {}".format(name, channel, type)
        # First {} a name, 2nd {} a channel, 3rd {} a type
print(a)
# Output:> This is Harry and his CodeWithHarry channel is Coding

print("_______________________________________________________________________________")

name = "Harry"
channel = "CodeWithHarry"
type = "Coding"

a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
        # First {} a name, 2nd {} a type, 3rd {} a channel
print(a)
# Output:> This is Harry and his Coding channel is CodeWithHarry