#Multiple Inheritane = inherit from more than one parent class
#                      C(A,B)

#multilevel Inheritance = inherit from a parent which inherit from another parent
#                      C(B) <- B(A) <- A

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")

class prey(Animal):
    def flee(self):
        print("prey is fleeing")
class predator(Animal):
    def hunt(self):
        print("predator is hunting")
class rabbit(prey):
    pass
class hawk(predator):
    pass
class fish(prey, predator):
    pass

Rabbit= rabbit("Tom",27)
Rabbit.eat()
Rabbit.flee()

# Hawk= hawk()
Fish=fish("Mash",12)
Fish.hunt()
Fish.eat()
Fish.flee()
print(Fish.name)


















