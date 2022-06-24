a=100
i=1
sum=0
sum_even=sum
odd=0
sum_odd=odd
while a<=500:
    if a %2==0:
        sum_even=sum_even+a
    elif a%2!=0:
        sum_odd=sum_odd+a
    a=a+1
print(sum_even)
print(sum_odd)