#super()  = Function used in a child class to call methods from a parent class (superclass).
#           allows you to extend the functionality of the inherit methods.

class Shape:
    def __init__(self,color,filled):
        self.color= color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color,filled)
        self.width = width 

class Triangle(Shape): 
    def __init__(self, color, filled, base):
        super().__init__(color,filled)
        self.base = base


circle= Circle(color="red",filled=True,radius= 5)

print(circle.color)



