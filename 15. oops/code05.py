#Abstraction => hidden unnecessary chize

class Car :
    def __init__(self):
        self.brk=False
        self.acc=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.clutch=True
        print("Car Start...")

c=Car()
c.start()
