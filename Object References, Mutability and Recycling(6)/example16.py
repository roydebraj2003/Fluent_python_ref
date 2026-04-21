# Example 6-16. Watching the end of an object when no more references point to it
import weakref

s1 = {1, 2, 3}
s2 = s1 # Ref to s1
def bye():
    print("This is the end")
ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print("del s1 invoked")
print(ender.alive)

del s2
print(ender.alive)



