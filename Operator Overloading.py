class Time:
    def __init__(self,h=0,m=0):
        self.hour = h
        self.min=m
    def __add__(self,other):
        return Time(self.hour+other.hour,self.min+other.min)
    def __str__(self):
        return f"{self.hour} hours {self.min} mins"
t1 = Time(10,30)
t2 = Time(5,10)
print(t1+t2)

#all method in one code
class Number:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return Number(self.x + other.x)
    def __sub__(self, other):
        return Number(self.x - other.x)
    def __mul__(self, other):
        return Number(self.x * other.x)
    def __truediv__(self, other):
        return Number(self.x / other.x)
    def __floordiv__(self, other):
        return Number(self.x // other.x)
    def __mod__(self, other):
        return Number(self.x % other.x)
    def __pow__(self, other):
        return Number(self.x ** other.x)
    def __eq__(self, other):
        return self.x == other.x
    def __lt__(self, other):
        return self.x < other.x
    def __gt__(self, other):
        return self.x > other.x
    def __le__(self, other):
        return self.x <= other.x
    def __ge__(self, other):
        return self.x >= other.x
    def __ne__(self, other):
        return self.x != other.x
    def __neg__(self):
        return Number(-self.x)
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return f"Number({self.x})"

a = Number(10)
b = Number(3)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Less Than:", a < b)
print("Greater Than:", a > b)
print("Less or Equal:", a <= b)
print("Greater or Equal:", a >= b)

print("Negative:", -a)
print("String:", str(a))
print("Representation:", repr(a))


#-----------
class Time:
    def __init__(self,h=0,m=0):
        self.hour = h
        self.min=m
    def __le__(self,other):
        return self.min <= other.min if self.hour==other.hour else self.hour<other.hour
    def __str__(self):
        return f"{self.hour} hours {self.min} mins"
t1 = Time(5,10)
t2 = Time(5,5)
t3 = Time(4,5)
t4 = Time(6,10)
t5 = Time(5,11)
print(t2<=t1)
print(t3<=t1)
print(t4<=t1)
print(t5<=t1)

#-------
class Time:
    def __init__(self,h=0,m=0):
        self.hour = h
        self.min=m
    def __add__(self,other):
        if isinstance(other,type(self)):
            return Time(self.hour+other.hour,self.min+other.min)
        elif isinstance(other,type(3)):
            return Time(self.hour+other,self.min)
        else:
            return None
    def __str__(self):
        return f"{self.hour} hours {self.min} mins"
t1 = Time(5,10)
print(t1+5)














