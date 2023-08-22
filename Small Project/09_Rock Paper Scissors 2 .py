import random

# Rock Paper Scissors
def gameWin(comp, you):
    if comp == you:
        print('None')
    elif comp == 's' and you=='p':
            print("Lose")
    elif comp == 's' and you=='r':
            print("Win")
    elif comp == 'r' and you=='s':
            print("Lose")
    elif comp == 'r' and you=='p':
            print("Win")
    elif comp == 'p' and you=='r':
            print("Lose")
    elif comp == 'p' and you=='s':
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
