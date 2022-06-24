a=1
sum=0
sum_odd=0
while a<=10:
    if a%2==0:
        sum=sum+a
    elif a%2!=0:
        sum_odd=sum_odd+a
    a=a+1
print(sum)
print(sum_odd)