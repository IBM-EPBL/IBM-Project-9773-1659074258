x=int(input())
a=0
b=1
if(x<0):
    print("Enter a Input")
elif(x==0):
    print(a)
elif(x==1):
    print(a)
    print(b)
else:
    print(a)
    print(b)
    while(True):
        tmp=b
        b=a+b
        a=tmp
        if(b<=x):
            print(b)
        else :
            break
