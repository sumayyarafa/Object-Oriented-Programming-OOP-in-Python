"""
Inheritance is a way to form new classes using classes that have
already been defined.

The new classes, known as derived classes, take over (or inherit)
attributes and behavior of the pre-existing classes, which are referred
to as base classes (or ancestor classes).

It is intended to help reuse existing code with little or no modification.
A class can be extended or subclassed
The class that is extended is a super class / parent class.
Some people use the words parent class or base class to mean a
super class
The extended class is a sub class or extended class or child class of
its super class.
An object created from the sub class has its own copy of all the
non-static fields defined in its super class
"""



class grandpapa:
   def __init__(self):
       print("creating grandpapa")
   def drive(self, count):
       print("Driving bus with ", count, " person")

class father(grandpapa):
   def drive(self, count):
       if count <= 8:
           print("Driving NOah with ", count, " person")
       else:
           print("Driving NOah with ", 8, " person")
           super().drive(count - 8)
class child(father):
   def __init__(self):
       pass
   def drive(self, count):
       if count <= 2:
           print("Driving Lambo with ", count, " person")
       else:
           print("Driving Lambo with ", 2, " person")
           super().drive(count - 2)

c = child()
c.drive(50)

#multiple inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def fetch(self):
        print("Labrador fetches")

# Using the classes
labrador = Labrador()
labrador.speak() # Inherits from Animal
labrador.bark() # Inherits from Dog
labrador.fetch() # Specific to Labrador

#The diamond probem
#The ”diamond problem” occurs when a class inherits from two classes that have a common ancestor. This can lead to ambiguity in method resolution.

class A:
    def greet(self):
        print("Hello from class A")
class B(A):
    def greet(self):
        print("Hello from class B")
class C(A):
    def greet(self):
        print("Hello from class C")
class D(B, C):
    pass
# Using the classes
obj = D()
obj.greet() # What will this print?








