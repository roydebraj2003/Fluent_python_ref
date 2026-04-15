""" Example 1-2 is a Vector class implementing the operations just described, through
the use of the special methods __repr__, __abs__, __add__, and __mul__. """

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __bool__(self): # __bool__ allows your objects to follow the truth value testing according to python standard
        return bool(self.x or self.y)
    def __rmul__(self, scaler):
        return self.__mul__(scaler)

v1 = Vector() #Default
v2 = Vector(3, 5)
v3 = Vector(5, 2)
# scaler * vecor will give an error to handle that we have to implement __rmul__
print(v2 + v3)
print(v3 * 4)
print(3 * v3)
print(abs(v2))
