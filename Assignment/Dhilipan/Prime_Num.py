import math
def prime(x):
    if(x<=0):
        print("Enter a Valid Input") 
    elif(x==1):
        print("1")
    elif(x==2):
        print("1")
        print("2")
    else:
        print("1")
        for i in range(2,x+1):
            val=True
            for j in range(2,int(math.sqrt(i))+1):
                 if(i%j==0):
                     val=False
                     break
            if(val==True):
                print(i)
prime(int(input()))

