# class variable = shared among all instance of a class 
#                  defined outside the constructor
#                  Allow you to share data among all objects created from that class 

class Car:
    wheels =4
    total_car= 0                      # class variable 
    
    def __init__(self, model, year):
        self.model = model           #instance variable
        self.year = year
        self.mileage = 0
        Car.total_car +=1
    
    def status(self):
        print(f"Model: {self.model}, Year: {self.year}" )

car1= Car("toyota", 2014)
car2= Car("honda", 2015)
car3= Car("BMW", 2024)

print(car1.wheels)
print(Car.wheels)

print(Car.total_car)