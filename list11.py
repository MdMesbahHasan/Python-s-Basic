words=0
letters=0
digits=0
txt=input("Enter the text: ")
for i in txt:
    i=i.lower()
    if i>='a' and i<='z':
        letters+=1
    elif i>='0' and i<='9':
        digits+=1
    elif i==" ":
        words+=1
print("Letters: ",letters)
print("Digits: ",digits)
print("Words: ",words+1)