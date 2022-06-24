num=int(input("enter number"))
rev=0
while 0<num:
    a=num%10
    num=num//10
    rev=rev*10+a
    print(rev)