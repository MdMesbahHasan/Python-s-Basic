try:
    a=int(input("Enter an integer: "))
    b=int(input("Enter second integer: "))
    r=a/b
    print(r)
except ValueError:
    print("Have to put an integer.")
except ZeroDivisionError:
    print("You can not divide it by zero.")
finally:
    print("Successful")