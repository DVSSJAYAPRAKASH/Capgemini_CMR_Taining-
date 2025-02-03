from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def max_speed(self):
        pass
    def __init__(self):
        self.brand=input("Enter the brand: ")
class Car(Vehicle):
    def max_speed(self):
        print(f"{self.brand} Car max_speed is 200kmph!")
class Bike(Vehicle):
    def max_speed(self):
        print(f"{self.brand} Bike max_speed is 150kmph!")
def main():
    car=Car()
    car.max_speed()
    bike=Bike()
    bike.max_speed()
main()