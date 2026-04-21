# Garbage collection and the del operator -  del is not a function it is a statement but del x and del(x) works in python


a = [1, 2, 3, 4]
b = a # b referes to a
del a

print(b)
b = [3] # b referes to a different list - The garbage collector will destroy the object as there are no reference to the list
print(a)
""" [1, 2, 3, 4]
Traceback (most recent call last):
  File "/home/roy/learning/Python/Object References, Mutability and Recycling(6)/example8.py", line 10, in <module>
    print(a)
          ^
NameError: name 'a' is not defined"""
