print("TEMPERATURE CONVERTER")
print("1.CELSIUS TO FARANHEIT")
print("2.FARANHEIT TO CELSIUS")
w=int(input("ENTER YOUR CHOICE:"))
if w==1:
    e=float(input("ENTER THE TEMPERATURE IN CELSIUS:"))
    r=(e*(9/5))+32
    print("THE GIVEN TEMPERATURE IN FARANHEIT IS:",r,"F")
elif w==2:
    t=float(input("ENTER THE TEMPERATURE IN FARANHEIT:"))
    y=((t-32)*(5/9))
    print("THE GIVEN TEMPERATURE IN CELSIUS IS:",y,"C")
else:
    print("SELECT ONLY THE GIVEN OPTIONS")