i=1
a=int(input("enter 1st num"))
while i<=a:
    b=int(input("enter 2nd num"))
    i=i+1
    if b==a:
        print("guessed right")
        break
    else:
        print("guessed wrong")
