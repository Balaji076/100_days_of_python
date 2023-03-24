print("ODD OR EVEN")
s=int(input("PLAYER 1 HAS TO CHOOSE: \n 1) ODD \n 2) EVEN \n SELECT ONE NUMBER:"))
if s==1:
    print("THE PLAYER 1 CHOOSES ODD")
    n=int(input("ENTER THE PLAYER 1 NUMBER:"))
    u=int(input("ENTER THE PLAYER 2 NUMBER:"))
    t=n+u
    if t%2 != 0:
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
elif s==2:
    print("THE PLAYER 1 CHOOSES EVEN")
    n=int(input("ENTER THE PLAYER 1 NUMBER:"))
    u=int(input("ENTER THE PLAYER 2 NUMBER:"))
    t=n+u
    if t%2 == 0:
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
else:
    print("PLEASE ENTER OPTIONS 1 OR 2")   