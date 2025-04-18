# Object = A "Bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup, book
#         You need a "class" to create many objects 

# Class = A blueprint or template for creating objects

from car import Car

print(Car.year)       # Output= 2020

car1=Car("mustang", 2024, "red", False)
print(car1.model)     # Output= mustang
print(car1.year)      # Output= 2024

car2=Car("BYD", 2025, "White", True)
print(car2.model)     # Output= BYD
print(car2.year)      # Output= 2025
car2.drive()          # Output= You drive the car

car3=Car("BMW-M3", 2021, "Black", True)
print(car3.model)     # Output: BMW-M3
car3.stop()
car3.describe()

















