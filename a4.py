n1=(input("enter the 1 input"))
n2=(input("Enter the 2 input"))
c=0
'''for i in range (len(n1) or len(n2)):
    if(n1.count(n1[i])== n2.count(n2[i])):
        
        print("0")
    else:
        c=c+1

    print(c)
   '''
#man
#mani
if(len(n1)>len(n2)):
    print(len(n1)-len(n2))
elif(len(n2)>len(n1)):
    print(len(n2)-len(n1))
elif len(n1)==len(n2):
    for i in range (len(n1) or len(n2)):
        if(n1[i]!=n2[i]):
            c=c+1
    print(c)
    
 
    