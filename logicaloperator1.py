a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))
c=float(input("Enter the third value: "))
if a>b and a>c:
    print(a," is the largest value")
elif b>a and b>c:
    print(b," is the largest")
else:
    print(c," is the largest.")
