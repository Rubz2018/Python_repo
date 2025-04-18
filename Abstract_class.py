# Abstract Class =A class that cannot be installed on it's own; meant to be sub-classed
#                 They can contain abstract methods, which are declared but have no implementation   
#                 Abstracts class benefits:
#                 1. prevent instantiation of hte class itself
#                 2. requires children to use inherited abstract methods
#

from abc import ABC, abstractmethod

# 🔷 Abstract Base Class
class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# 🚗 ElectricCar subclass
class ElectricCar(Car):
    def start_engine(self):
        print("Electric engine started silently.")

    def drive(self):
        print("ElectricCar is now driving smoothly...")

# 🚙 DieselCar subclass
class DieselCar(Car):
    def start_engine(self):
        print("Diesel engine rumbles to life!")

    def drive(self):
        print("DieselCar is now roaring down the road...")

# 🚀 Common test drive function
# def test_drive(car: Car):
#     car.start_engine()
#     car.drive()

# 🧪 Create instances and test
tesla = ElectricCar()
jeep = DieselCar()

# test_drive(tesla)
# print("---")
# test_drive(jeep)

tesla.start_engine()
