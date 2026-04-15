""" Generator Expressions
To initialize tuples, arrays, and other types of sequences, you could also start from a
listcomp, but a genexp (generator expression) saves memory because it yields items
one by one using the iterator protocol instead of building a whole list just to feed
another constructor.
Genexps use the same syntax as listcomps, but are enclosed in parentheses rather
than brackets.
Example 2-5 shows basic usage of genexps to build a tuple and an array.
Example 2-5. Initializing a tuple and an array from a generator expression """
import array
symbols = '$¢£¥€¤'
a = tuple((ord(x) for x in symbols))
b = array.array('I',(ord(x) for x in symbols)) #array(typecode [, initializer]) -> array, I is for unsigned integer
print(a)
print(b)
