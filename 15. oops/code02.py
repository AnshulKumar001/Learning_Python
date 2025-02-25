class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database")
s1=Student("Anshul",97)   
print(s1.name,s1.marks) 

s2=Student("Anu",90)
print(s2.name,s2.marks)

s3=Student("Abhi",100)
print(s3.name,s3.marks)