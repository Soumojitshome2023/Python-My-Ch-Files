# Rock Paper Scissors
n1 = input("Player 1 Enter Your Name: ")
n2 = input("Player 2 Enter Your Name: ")

def gameWin(p1, p2):
    if p1 == p2:
        print('None')
    elif p1 == 's' and p2=='p':
            print(n1 + " Win")
            print(n2 + " Lose")
    elif p1 == 's' and p2=='r':
            print(n1 + " Lose")
            print(n2 + " Win")
    elif p1 == 'r' and p2=='s':
            print(n1 + " Win")
            print(n2 + " Lose")
    elif p1 == 'r' and p2=='p':
            print(n1 + " Lose")
            print(n2 + " Win")
    elif p1 == 'p' and p2=='r':
            print(n1 + " Win")
            print(n2 + " Lose")
    elif p1 == 'p' and p2=='s':
            print(n1 + " Lose")
            print(n2 + " Win")
    else :
        print("Invalid Input")

p7 = input( n1 + "'s Turn: Rock(R), Paper(P) Scissors(S) ?")
p5 = input( n2 + "'s Turn: Rock(R), Paper(P) Scissors(S) ?")
gameWin(p7, p5)

print("Thank You " + n1 + " and " + n2)