i=1
a=int(input("enter a"))   
while a<=5:
    b=int(input("enter b"))
    if b==a:
        print("you hv guessed is rgh")
        a+=1
        break
else:
    print("you loss your 5 chance")    
    