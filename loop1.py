list=[1,2,3,4,5,6,7,8,9,0]
i=0
sum=0
while i<10:
    print(list[i])
    i+=1
print("By for loop")
for i in list:
    sum=sum+i
    print(i)
    #i+=1
print("The summation of the values is: ",sum)