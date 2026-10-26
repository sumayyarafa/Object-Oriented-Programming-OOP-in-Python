'''Abstract Class is a class that is not intended to be instantiated
directly, but only to be used as a base class by one or more subclasses.
Abstract Method is a method that must be overridden in every
subclass. '''
from abc import ABC, abstractmethod

from anyio import value

class Person(ABC):
   def __init__(self, name, email):
       self.name = name
       self.email = email

   @abstractmethod
   def print_details(self):
       pass

class Teacher(Person):
   def __init__(self, name, email, designation):
       super().__init__(name, email)
       self.designation = designation
   def print_details(self, kk):
       print(self.name, self.email)
t = Teacher("salma ", "a@gmail.com", "Lecturer")
t.print_details("kk")

#Class Methods 
#A classmethod is a method that is bound to the class. It takes the class as its first argument (cls). This allows the method to access and modify class-level variables and perform operations related to the class.

class MyClass:
    class_variable = "Class Variable"
    def __init__(self, value):
        self.instance_variable = value
    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Accessing class variable:", cls.class_variable)
    def instance_method(self):
        print("This is an instance method")
        print("Accessing instance variable:", self.instance_variable)

MyClass.class_method()
obj = MyClass("Instance Variable")
obj.instance_method()
obj.class_method()


#A common use case for a class method in Python is to provide alternative constructors.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name.strip(), int(age))
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
# Creating a Person instance using the constructor
person1 = Person("Alice", 30)
print(person1)
# Creating a Person instance using the class method
person2 = Person.from_string("Bob,25")
print(person2)

#Static Methods
'''Static methods are methods that belong to a class but do not operate on
the instance or class. They are defined using the @staticmethod decorator.
Static methods do not implicitly receive a reference to either the instance
or the class as their first argument (i.e., self or cls).'''

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day}/{self.month}/{self.year}"

    @staticmethod
    def is_valid_date(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 0:
            return True
        return False

print(Date.is_valid_date(31, 12, 2023))
print(Date.is_valid_date(32, 13, 2023))

#encapsulation
#Encapsulation is the principle of bundling the data (attributes) and the methods that operate on that data into a single unit (the class). It also involves restricting direct access to some of an object’s components, preventing external code from accidentally corrupting the internal state.

'''Python relies on naming conventions to suggest access control:
        • Single Leading Underscore (_name): This is a convention for a private attribute or
        method. It tells other programmers "This is for internal use; please do not access or modify
        it directly." Python does not prevent external access.
        • Double Leading Underscore (__name): This triggers name mangling, where Python
        changes the attribute name internally (e.g., __balance becomes _Account__balance). While it
        can be accessed externally, it makes it harder and is a stronger signal of privacy.'''

class Account:
    def __init__(self, initial_balance):
        # "Private" attribute (name mangling)
        self.__balance = initial_balance
        # "Protected" attribute (convention)
        self._owner_name = "Anonymous"
    # Public method to access the balance
    def get_balance(self):
        return self.__balance
    # "Private" method (name mangling)
    def __update_balance(self, amount):
        self.__balance += amount
        print("Balance updated internally.")

    def deposit(self, amount):
        if amount > 0:
            # We call the private method internally
            self.__update_balance(amount)

acc = Account(500)
acc.deposit(100)
print(f"Current Balance: {acc.get_balance()}")

# External attempts (Discouraged/Failed/Difficult)
print(f"Owner Name (Access discouraged): {acc._owner_name}")
print(f"Owner Name (Access discouraged): {acc._Account__balance}")

#Accessing mangled attribute (Technically possible, but bad practice)
# print(f"Mangled Balance: {acc._Account__balance}")














