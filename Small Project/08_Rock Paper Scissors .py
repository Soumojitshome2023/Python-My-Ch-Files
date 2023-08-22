import random

# Rock Paper Scissors
def gameWin(comp, you):
    if comp == you:
        print('None')
    elif comp == 's':
        if you=='p':
            print("Lose")
        elif you=='r':
            print("Win")
    elif comp == 'r':
        if you=='s':
            print("Lose")
        elif you=='p':
            print("Win")
    elif comp == 'p':
        if you=='r':
            print("Lose")
        elif you=='s':
            print("Win")

randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(R), Paper(P) Scissors(S) ?")
gameWin(comp, you)

print(f"Computer chose {comp}")
