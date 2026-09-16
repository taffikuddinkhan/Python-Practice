class Car:  # parent class

    color = "black"

    @staticmethod   # Decorator
    def start():
        print("starting")

    @staticmethod
    def stop():
        print("stopped")

class Toyota(Car): #child class , inherits the parent class Car
    def __init__(self,name):
        self.name=name
        print(self.name)

car1 = Toyota("fortuner") #object creation
car2 = Toyota("prius")
car1.start()  #parent class methods accessed by child class
car2.stop()
print(car1.color)  #accessing parent class attribute colour
print(car2.color)
