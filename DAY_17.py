print("GUESS THE WORDS ")
print("1.edb")
e=(input("FIND THE FIRST WORD:"))
g=0
if (e =='bed'):
    g=g+1
    print("YOU FOUND THE FIRST WORD SUCCESSFULLY")
    print("2.druen")
    y=input("FIND THE SECOND WORD:")
    if y =='under':
        g=g+1
        print("YOU FOUND THE SECOND WORD SUCCESSFULLY")
        print("3.stieus")
        r=input("FIND THE THIRD WORD:")
        if r=='tissue':
            g=g+1
            print("YOU FOUND THE THIRD WORD SUCCESSFULLY")
            print("4.koboento")
            v=input("FIND THE FOURTH WORD:")
            if v=='notebook':
                g=g+1
                print("YOU FOUND THE FOURTH WORD SUCCESSFULLY")
                print("5.listen")
                n=input("FIND THE FINAL WORD TO COMPLETE THE GAME:")
                if n=='silent':
                    g=g+1
                    print("YOU FINISHED THE GAME") 
    print(" YOUR SCORE IS ",g,"/5")
else:
    print("YOU LOST")