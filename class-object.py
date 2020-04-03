class Student:
    roll=""#roll and gpa common properties of the class.
    name=""
rahim=Student()#Object creation
print(isinstance(rahim,Student))#Here saying rahim is the object of student class,if it is then return true
#now rahim can use the properties of class
rahim.roll=101
rahim.name="Mesbah Hasan"
#When printing the value's we will use formatted function
print(f"Roll:{rahim.roll}, Name:{rahim.name}")
karim=Student()
print(isinstance(karim,Student))
karim.roll="102"
karim.name="Karim Hasan"
print(f"Roll:{karim.roll},Name:{karim.name}")