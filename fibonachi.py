i=0
a=0
b=1
c=0
print(a,b, end=" ")
n=int(input("enter num"))
while i<=10:
    c=a+b
    a=b
    b=c
    print(c, end =" ")
    i=i+1

