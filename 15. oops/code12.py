#super function
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car start..")

    @staticmethod
    def stop():
        print("stop Car..")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name  # Initialize the name attribute for ToyotaCar
        super().__init__(type)  # Initialize type in the Car class


car1 = ToyotaCar("Prius", "Diesel")
print(car1.type)  # Access type from the Car class
print(car1.name)  # Access name from the ToyotaCar class

        