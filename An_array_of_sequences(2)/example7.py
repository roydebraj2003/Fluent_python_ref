""" Example 2-7. Tuples used as records """

list_of_tuples = [(x, x*x) for x in range(1, 11)]

a = ('hearts', 'diamond', 'spades', 'club')

q, w, e, r = a
print(q, w,e , r)

# The % formatting operator understands tuples and treats each item as a separate field.
for var in list_of_tuples:
    print('%s, %s' %var)

""" The for loop knows how to retrieve the items of a tuple separately—this is called
“unpacking.” Here we are not interested in the second item, so we assign it to _, a
dummy variable."""

for _, sq in list_of_tuples:
    print(sq)

""" The content of the tuple itself is immutable, but that only means the refer‐
ences held by the tuple will always point to the same objects. However, if one of the ref‐
erenced objects is mutable—like a list—its content may change. """

t = ('a', 'b', [1, 2, 3])
m = ('a', 'b', [1, 2, 3])

print(t == m) # True

m[-1].append(99)

print(t == m) # False

# To check if hashable
# an object is only hashable if its value cannot ever change. An unhashable tuple cannot be inserted as a dict key, or a set element.

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

n = ('a', 'b', (1, 2, 3))
print(fixed(m))
print(fixed(n))
