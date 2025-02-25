
#Private function => password not access because password out of the class(password private __ ) 

class Account:
    def __init__(self,password,acc_no):
        self.acc_no=acc_no
        self.__password=password



acc1=Account("1234","12334556")
print(acc1.acc_no)
print(acc1.__password)