#Polymorphism means many forms. In OOP, it allows the same method, function, or interface to behave differently depending on the object or data it works with. 
#Same method name + different behavior = Polymorphism.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects
a1 = Dog()
a2 = Cat()
# Calling the same method
a1.sound()
a2.sound()