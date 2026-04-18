# Example 2-20. Handling 6 bytes of memory as 1×6, 2×3, and 3×2 views
from array import array
ar = bytearray([1, 2, 3, 4, 5, 6])
m1 = memoryview(ar)
sliced_array = m1[2 : 4]
print(sliced_array)

print(m1.tolist())

m2 = m1.cast('B', [2, 3]) # cast it to 2 rows and 3 columns
print(m2)

m2[1, 2] = 99
m2[0, 1] = 100
# Example 2-21. Changing the value of a 16-bit integer array item by poking one of its bytes

a = array('H', [1, 2, 3, 4, 5, 6])
mv = memoryview(a)
print(len(mv), mv.tolist())
mv2 = mv.cast('B')
print(len(mv2), mv2.tolist())
