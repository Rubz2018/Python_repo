# #Inheritance = Allows a class to inherit attributes and method from another class 
# # helps with code reusability and extensibility 
# # class child(Parent)

# class Father:
#     height =  182
#     color  = "red"

# class Son(Father):
#     pass

class Animal:
    def __init__(self, name):
        self.name= name
        self.is_alive= True
        
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak (self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak (self):
        print(f"{self.name} is barking")

class Mouse(Animal):
    def speak (self):
        print(f"{self.name} is barking")

dog= Dog("Scooby")
cat= Cat("TOm")
mouse= Mouse("Mickey")    


print(dog.name)
print(dog.is_alive)
#print(dog.height)  #AttributeError: 'Dog' object has no attribute 'height 

dog.eat()
dog.sleep()  #Dog is sleeping


dog.speak()




