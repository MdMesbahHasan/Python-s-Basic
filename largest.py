a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
"""
if a>b:
    if a>c:
        print(a ," is the largest")
    else:
        print(c ,"is the largest")
if(b>a):
    if(b>c):
        print(b ," is the largest")
    else:
        print(c," is the largest")
    """
    ##Ternary Operator
max=a if a>b else b
print("Maximum between first two numbers:",max)