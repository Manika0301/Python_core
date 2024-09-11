import arithematic as a1
import sys
while True:

    print("1.Add")

    print("2.sub")
    print("3.Mul")
    print("4.Div")
    n=int(input("Enter your choice: "))
    if(n==1):
        a1.add(1,2)
    if(n==2):
        a1.sub(3,2)
    if(n==3):
        a1.mul(1,2)
    if(n==4):
        a1.div(2,1)
    if(n==0):
        sys.exit(0)
