# Polymorphism = Greek word that means to " have many form or faces "
#               poly = many
#               mporhe = form 

#       Two ways to achieve Polymorphism
#       1. Inheritance = An object could be treated of the same type as a parent class
#       2. "Duck typing" = Object must have necessary attributes / methods


from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
class rectangle(Shape):
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
class Triangle(Shape):
    def __init__(self,a):
        self.a = a
    def area(self):
        return 0.5 * (self.a ** 2)
class Pizza(Circle):
    def __init__(self,peparroni, radius):
        super().__init__(radius)
        self.peparroni = peparroni
    

shape= Pizza("topping", 15)
print(shape.area())

shapes = [Circle(4), rectangle(5,6), Triangle(3), Pizza("toppings", 13)]

for shap in shapes:
    print(f"{shap.area()}cm²")



# pizza -> pizza + circle + shape => many forms (polymorphism)

