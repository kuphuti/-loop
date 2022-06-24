a=int(input("enter number"))
p=a
rev=0
while p>0:
    b=p%10
    p=p//10
    rev=rev*10+b
    print(rev)
if a==rev:
    print("its palimdrom")
else:
    print("not palimdrom")