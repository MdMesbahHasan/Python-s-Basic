#Exception handling by just one block
try:
    a=int(input("Enter an integer: "))
    b=int(input("Enter second integer: "))
    r=a/b
    print(r)
except (ValueError,ZeroDivisionError):
    print("You did put a wrong input")
finally:
    print("Successful")