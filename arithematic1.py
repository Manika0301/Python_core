def arm(n):
    sum=0
    temp=n
    while(temp>0):
        temp=temp%10
        
        sum=sum+temp**3
        temp=temp//10
    if(sum==n):
        print("armstrong num:")
    else:
        print("not arm:")
    
def palin(n):
    temp=n
    rev=0
    rem=0
    while(temp>n):
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if(rev==n):
        print("Yes:")
    else:
        print("Not palindrome")
def factor(n):
    for i in range(len(n)):
        if(n%i==0):
            print("factor:")
        else:
            print(i,"is not the factor")


    
def rev(a,b):
    print("Division is :", a//b)
