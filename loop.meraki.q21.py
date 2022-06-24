i=0
sum=0
c=int(input("enter c"))
average=0
while i<=c:
    a=int(input("enter a"))
    sum=sum+a
    i=i+1
total_sum=sum
total_average=sum%c
if total_average%5==0:
    print("it is divisible by 5")
else:
    print("it is not divisible by 5")
