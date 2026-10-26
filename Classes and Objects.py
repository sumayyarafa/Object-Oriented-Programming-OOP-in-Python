#Adding attributes to an object
from operator import add, sub
class Student:
    pass

Alice = Student()
Alice.firstName = 'Diana'
Alice.lastName = "Alice"
Alice.age = 41
Alice.adress = "Dhaka"
Alice.weight = 71.2
Alice.cgpa = 3.75
print(f'{Alice.firstName} {Alice.lastName}')
print(type(Alice))

#adding constructor to a class
class Student:
    def __init__(self):
        self.firstName = "Diana"
        self.lastName = "Alice"
        self.age = 41
        self.adress = "Dhaka"
        self.weight = 71.2
        self.cgpa = 3.75

Alice = Student()
print(f'{Alice.firstName} {Alice.lastName}')

#adding constructor with parameters to a class
#Default parameters must come at the end of the parameter list.
class Student:
    university = "UIU"
    def __init__(self,fname,lname,age,address,weight,cgpa=0.0):
        self.firstName = fname
        self.lastName = lname
        self.age = age
        self.adress = address
        self.weight = weight
        self.cgpa = cgpa

Alice = Student("Diana","Alice",41,"Dhaka",71.2)
farid = Student("Dewan Md","Farid",45,"Dhaka",91.2,4.00)
print(f"{Alice.firstName}'s cgpa: {Alice.cgpa}")
print(f"{farid.firstName}'s cgpa: {farid.cgpa}")

#add display method to a class
class Account:
    def __init__( self):
        self.name = ""
        self.age=0
    def show(self):
        print("Name:",self.name,"Age:",self.age,"Department:")

ac = Account()
ac.name = "Alice"
ac.age = 41
ac.show()

#Objects as parameters

class Point:
    def __init__(self, xCor = 0, yCor=0):
        self.x = xCor
        self.y = yCor
    def show(self):
        print(f"({self.x},{self.y})")
def distance(p1,p2):
    return ((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))**0.5
print(distance(Point(4,3),Point()))

#Functions are objects
def myFunc():
    print("Hello My Func")
def runFunc(x):
    x()
x = myFunc
runFunc(x)

#Returning Functions
def customFunc(x):
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    if x==1:
        return add
    else:
        return sub
f = customFunc(1)
print(f(1,3))


#___str__ method
#The __str__ () dunder method returns a reader-friendly string representation of a class object.

class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h
        print("I am a constructor")
    def getArea(self):
        return self.height*self.width
    def __str__(self):
        return f'width: {self.width} height: {self.height}'
r = Rectangle(4,12)
print(r)


#destructor
#The __del__ () dunder method is called when an object is about to be destroyed
class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h
        print("I am a constructor")
    def getArea(self):
        return self.height*self.width
    def __str__(self):
        return f'width: {self.width} height: {self.height}'
    def __del__(self):
        print("I am a destructor")
r = Rectangle(4,12)
del r

#__repr__ method
#The __repr__ () dunder method returns an unambiguous string representation of a class object. It is used for debugging and development purposes.
#The main difference is:
#           - __str__() → when you want to show information to a normal user.
#           - __repr__() → when you want a clear, unambiguous representation for developers, debugging, or inspecting objects.
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def __str__(self):
        return f"Student name: {self.name}"
    def __repr__(self):
        return f"Student('{self.name}', {self.student_id})"

s1 = Student("Kotha", 101)
print(s1)
print(repr(s1))




















