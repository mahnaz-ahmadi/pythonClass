pattern=float(input("What pattern?"))
def hop():
    num1=1
    while num1<20:
        if num1%pattern==0:
            print("Hop")
            player=input()
            if (player)!=num1+1:
                print("What the hell is this? You lose !")
                break
                input()
            else:
                num1+=2
                continue
        else:
            print(num1)
            player=input()
            if (num1+1)%pattern==0 and player!="hop":
                print("Huh! You Loser!")
                break
            elif (num1+1)%pattern!=0 and player=="hop":
                print("Huh! You unlocky!")
                break
            else:
                num1+=2
    print("Ok! That's Enough!")
hop()
