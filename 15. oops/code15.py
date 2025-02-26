
#Polymorphism       operator overloading



class complex :
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def Show_no(self):
        print(self.real,"i +",self.img,"j")

num1=complex(2,5) 
num1.Show_no()       




#add 2 complex number
class complex :
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def Show_no(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2) :
        new_real=self.real+num2.real
        new_img=self.img+num2.img
        return complex(new_real,new_img) 
    

    def __sub__(self,num2):
        new_real=self.real-num2.real
        new_img=self.img-num2.img
        return complex(new_real,new_img) 



num1=complex(2,5) 
num1.Show_no()

num2=complex(45,67)
num2.Show_no()


num3=num1+num2
num3.Show_no()

num3=num1-num2
num3.Show_no()

