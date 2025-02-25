# inheritance (I have to pass the information of A class in other class)


#single inheritance 
class Car:
    @staticmethod
    def start():
        print("Car start..")


    @staticmethod
    def stop():
        print("stop Car..")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
car1=ToyotaCar("BMW")
car2=ToyotaCar("Prius")

print(car1.start())
print(car1.name)