i=1
a=4
while i<=5:
    b=int(input("enter b"))
    i=i+1
    if b<a:
        print("number is smaller")
    elif b>a:
        print("number is greater")    
    elif b==a:
        print("wow you geussed the correct number")    
        break
else:
    print("wrong number")    