import math
x=int(input())
if(x==1 or x==2):
    print("Prime")
elif(x==0):
    print("Not a Prime")
else:
    val=True
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            val=False
            break
    if(val==False):
        print("Not a Prime")
    else:
        print("Prime")