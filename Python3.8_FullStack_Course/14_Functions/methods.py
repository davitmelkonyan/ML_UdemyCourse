class Pizza(object):
    def __init__(self,size):
        self.size = size

    def get_size(self):
        return self.size

p  = Pizza(1)
print(p.get_size)
print(p.get_size())
print(Pizza.get_size(Pizza(24)))
m = Pizza(24).get_size
print (m())
print (m.__self__.get_size)
print (m.__self__)
print(m == m.__self__.get_size)

class D(object):
    mult = 20
    
    @classmethod
    def f(cls,x):
        return cls.mult*x
    
    @staticmethod
    def g(name):
        print("HI %s"%name)

print (D.f) #bound
print (D.f(12))
print (D.g)
D.g('World')

l = [1,2,3,4,5]
#methods for a list :append,count,extend,insert,pop, remove, reverse,sort

class Shape(object):
    #classmethods can be overridden by inherited classes
    @classmethod
    def from_square(cls, square):
        return cls() #default instance

class Square(Shape):
    def __init__(self, side=10):
        self.side = side

    @classmethod
    def from_square(cls, square):
        return cls(side=square.side)


class Rectangle(Shape):
    def __init__(self, length=10, width=10):
        self.length = length
        self.width = width

    @classmethod
    def from_square(cls, square):
        return cls(length=square.side, width=square.side)


class RightTriangle(Shape):
    def __init(self, a=10, b=10):
        self.a = a
        self.b = b
        self.c = ((a*a) + (b*b))**(.5)

    @classmethod
    def from_square(cls, square):
        return cls(a=square.length, b=square.width)


class Circle(Shape):
    def __init__(self, radius=10):
        self.radius = radius

    @classmethod
    def from_square(cls, square):
        return cls(radius=square.length/2)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)