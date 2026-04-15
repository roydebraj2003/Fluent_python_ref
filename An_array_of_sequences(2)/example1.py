from collections import abc
print(issubclass(tuple, abc.Sequence)) #True
print(issubclass(list, abc.MutableSequence)) #True

symbols = '$¢£¥€¤'
ascii_val = []
for symbol in symbols:
    ascii_val.append(ord(symbol))

print(ascii_val)

print([ord(x) for x in symbols]) # List comprehension - can be multiline
