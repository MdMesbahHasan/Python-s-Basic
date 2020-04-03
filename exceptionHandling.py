#finally keyword must work if no part of the code works..it does work for every exception
#It is not able to handle the exception but it does execute
try:
    list=[20,10,0]
    result=list[1]/list[2]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
finally:
    print("Will not work")
