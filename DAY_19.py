print("CHECK FOR PRIME NUMBER")
b=int(input("ENTER THE NUMBER:"))
temp=False
if b>1:
    for i in range(2,b):
        if (b%i)==0:
            temp=True
            break
if(temp):
    print("THE NUMBER ",b,"IS NOT A PRIME NUMBER")
else:
    print("THE NUMBER",b,"IS A PRIME NUMBER")