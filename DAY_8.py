print("BODY MASS INDEX")
h=float(input("ENTER YOUR HEIGHT (IN METERS):" ))
w=float(input("ENTER YOUR WEIGHT (IN KILOGRAMS:"))
b=w/(h**2)
print("THE BODY MASS INDEX IS:",b)
if b>25:
    print("KEEP YOUR WEIGHT IN CONTROL")
elif b<19:
    print("INCREASE YOUR WEIGHT ")
else:
    print(" JUST MAINTAIN YOUR WEIGHT")