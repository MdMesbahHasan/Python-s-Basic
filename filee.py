file=open("student.txt","r")
print(file.readable())
txt=file.read()
print(txt)
size=len(txt)
print(size)
for lines in file:
    print(lines)

file.close()