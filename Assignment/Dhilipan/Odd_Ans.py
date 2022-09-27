x=int(input())
a1=0
a2=1
if(x<0):
  print("Enter a Valid Input")
elif(x==0):
  print(a1)
elif(x==1):
  print(a1)
  print(a2)
else:
  print(a1)
  print(a2)
  while(True):
    temp=a2
    a2=a1+a2
    a1=temp
    if(a2<=x):
      print(a2)
     else :
      break
      
