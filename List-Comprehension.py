#Basic structure::[exprssion for item in list]
num=[1,2,3,4,5]
a=[x*x for x in num]
print(a)
b=[x for x in num if x%2==0]
c=[x for x in num if x<0]
print(b)
print(c)