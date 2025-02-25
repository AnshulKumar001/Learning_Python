class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hii",self.name,"your average score is :",sum/3)
s1=Student("Anu ",[89,90,98])  
s1.avg()  
s1.name="Anshul"
s1.avg()