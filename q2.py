# Q2. Create Abstract class Vehicle with: (4 Marks) 
# • Abstract methods: start(), stop(), fuel_type() 
# Create 3 child classes:
# • Car → 'Car started' / 'Petrol'
# • Bike → 'Bike started' / 'Petrol'
# • Tesla → 'Tesla started' / 'Electric' 
# Create objects and call all methods.

from abc import ABC,abstractmethod

class vehicle(ABC):
    def start(self):
        pass

    def stop(self):
        pass
    def fuel_type(self):
        pass 
class car(vehicle):
    def start(self):
        print("car stated")
    def stop(self):
        print("car is stop")
    def fuel_type(self):
        print("petrol car")
class bike(vehicle):
    def start(self):
        print("bike is started")
    def stop(self):
        print("bike is stop")
    def fuel_type(self):
        print("PETROL bIKE")
class Tesla(vehicle):
    def statr(self):
        print("Tesla started")

    def stop(self):
        print("Tesla stopped")

    def fuel_type(self):
        print("Electric")
car = car()
bike = bike()
Tesla = Tesla()

car.fuel_type()
car.start()
car.stop()

bike.start()
bike.stop()
bike.fuel_type()

Tesla.start()
Tesla.stop()
Tesla.fuel_type()