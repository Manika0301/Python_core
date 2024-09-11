a=[]
a=list(eval(input("Enter the array")))
temp=0
i=0
j=1
for i,j in range(len(a)):
  
  if(a[i]==0):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
  else:
    i=i+1
    j=j+1
print(a)
