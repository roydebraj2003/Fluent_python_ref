# Example 6-2. Variables are bound to objects only after the objects are created

class foo():
    def __init__(self):
        print(f'foo() id {id(self)}')

print(foo()) # Prints id

y = foo() * 10
print(y)
