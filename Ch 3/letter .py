letter = ''' dear <|name|>,
you are selected

date = <|date|>
'''
name = input("enter your name")
date = input("enter date")

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)

print(letter)