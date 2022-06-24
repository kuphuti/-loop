a=100
sum_even=0
sum_odd=0
while a<=500:
    if a%2==0:
       sum_even=sum_even+a
    elif a%2!=0:
       sum_odd=sum_odd+a 
    a=a+1
print(-sum_even)  
print(sum_odd)  
