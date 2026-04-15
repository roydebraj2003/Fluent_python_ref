""" Example 2-3. The same list built by a listcomp and a map/filter composition """

# List comprehention vs map/filter
# Listcomp are much faster than map/filter
symbols = '$¢£¥€¤'
beyond_ascii = [ord(x) for x in symbols if ord(x) > 127]

""" map(func, *iterables) --> map object
    filter(function or None, iterable) --> filter object
"""

a = list(filter(lambda x : x > 127, map(ord, symbols)))
print(a)
print(beyond_ascii)
