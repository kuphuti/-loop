a=input("enter")
i=0
arm=0
while i<len(a):
    b=a[i]
    c=(int(b)**3)
    arm=c+arm
    i=i+1
print(arm) 
if int(a)==arm:
    print("arm")
else:
    print("not arm")    


    
    