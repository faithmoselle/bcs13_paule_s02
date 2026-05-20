'''class A:
    def __init__(self):
        self.x=1

class B(A):
    def __init__(self):
        super().__init__()
        self.y =2

obj = B()
print(obj.x, obj.y)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "Circle with radius " + str(self.radius)


c = Circle(3)
print(c)


class A:
    def display(self):
        print("Class A")


class B(A):
    pass


obj = B()
obj.display()


class A:
    def display(self):
        print("Class A")


class B(A):
    def display(self):
        print("Class B")


obj = B()
obj.display()

class A:
    def display(self):
        print("Class A")


class B(A):
    pass


obj1 = A()
obj2 = B()
obj1.display()
obj2.display()


class A:
    def __init__(self):
        self.x = 1


class B:
    def __init__(self):
        super().__init__()
        self.x = 2


obj = B()
print(obj.x)


class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, y):
        super().__init__(y)


obj = B(5)
print(obj.x)


class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, y):
        super().__init__(y)
        self.y = y


obj = B(10)
print(obj.x, obj.y)


class A:
    def __init__(self):
        self.x = 1


class B(A):
    pass


obj = B()
print(obj.x)


class A:
    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super().__init__()
        self.x = 2


obj = B()
print(obj.x)


class A:
    def __init__(self):
        self.x = 1


class B(A):
    pass


obj = B()
print(obj.x)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

r  = Rectangle(4,5)
print(r.area())


class A:
    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super().__init__()

class A:
    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2


obj = B()
print(obj.x, obj.y)


class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, y):
        super().__init__( y)


obj = B(5)
print(obj.x)


class A:
    def display(self):
        print("Class A")


class B(A):
    def display(self):
        print("Class B")


obj1 = A()
obj2 = B()
obj1.display()
obj2.display()'''


class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, y):
        super().__init__(y)
        self.y = y


obj = B(10)
print(obj.x, obj.y)
