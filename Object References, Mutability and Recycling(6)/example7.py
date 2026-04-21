# Shallow copy and deep copy

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
            # This will make the original passengers list mutate to avoid this we need to make a copy of it list(passengers)
            # To make shallow copy we can use the copy module, slicing [:] or built in constructor like list() dict() 

    def pick(self, person):
        self.passengers.append(person)
    def drop(self, person):
        self.passengers.remove(person)

import copy

bus1 = Bus(['Mark', 'Alice', 'Nate', 'George', 'Roy'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

# Deep copy : duplicates do not share reference of nested objects, while shallow copy does
print(list(bus1.passengers), list(bus2.passengers), list(bus3.passengers))
bus1.drop('Mark')
print(list(bus1.passengers), list(bus2.passengers), list(bus3.passengers))
bus1.pick('xyz')
print(list(bus1.passengers), list(bus2.passengers), list(bus3.passengers))

# Cyclic reference
a = [1, 2]
b = [a, 3]
a.append(b)

print(a)

da = copy.deepcopy(a)
print(da)
