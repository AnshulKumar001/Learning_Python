
#Multilevel inheritance

class Car:
    @staticmethod
    def start():
        print("Car start..")


    @staticmethod
    def stop():
        print("stop Car..")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand


class BMW(ToyotaCar):
    def __init__(self, type):
        self.type=type

        
car1=BMW("Diesel")
car1.start()
print(car1.type)