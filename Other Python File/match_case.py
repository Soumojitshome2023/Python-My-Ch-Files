x = int(input("Enter 1 to 3 number : "))

match x:
    case 1:
        print("you enter 1")

    case 2 :
        print("you enter 2")
        
    case 3 :
        print("you enter 3")

    case _:
        print(x)