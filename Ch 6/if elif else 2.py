age = input("what is your age ? ")
if int(age) >= 18:
    print("you are an adult")
    print("you can vote")
elif int(age) < 18 and int(age) > 3:
    print("you are in school")
else:
    print("you are a child")


print("thank you")