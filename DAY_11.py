print("CHECKING PRIME NUMBER")
a=int(input("ENTER THE NUMBER:"))
if a ==1:
    print("THE GIVEN NUMBER IS NOT A PRIME NUMBER")
elif a>1:
    for i in range(2,a):
        if a%i==0:
            print("THE GIVEN NUMBER IS NOT A PRIME NUMBER")
            break
    else:
        print("THE NUMBER IS A PRIME NUMBER")
else:
    print("THE NUMBER IS NOT A PRIME NUMBER")
    