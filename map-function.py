#We can pass a function and a list in the map function
def square(x):
    return x*x
num=[1,2,3,4,5]
r=list(map(square,num))
print(r)

#Now the use of filter function
d=list(filter(lambda x:x%2==0,num))
print(d)