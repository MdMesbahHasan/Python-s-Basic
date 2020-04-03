#User defined function
def sum(a,b):
    s=a+b
    print(s)
sum(3,4)
sum(9,10)
sum(1121,1212)
def multiplication(x,y):
    m=x*y
    print(m)

multiplication(12,12)
def lines():
    print("This is user defined function")
lines()
def inputt():
    b=int(input("Take integer value 01: "))
    c = int(input("Take integer value 02: "))
    s=b+c*b
    print(s)
inputt()

def add(a,b):
    s=a+b
    return s
print(add(12,1111))

def largest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>a:
            if b>c:
                return b
            else:
                return c
print(largest(122.5666,122.567,18.1212121212121))