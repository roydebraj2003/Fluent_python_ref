lst = [1, 2, 3, 4, 5]
id_before = id(lst)
lst = lst + [6, 7]
id_after = id(id)

print(id_before == id_after) #False
ls = [1, 2, 3]
id1 = id(ls)
ls += [4, 5]
id2 = id(ls)
print(id1 == id2) #True
# Example 2.16
t = (1, 2, [30, 40])
#t[2] += [50, 60]
print(t) # (1, 2, [30, 40, 50, 60])
import dis
s = [[1, 2, 3],  4, 5]
print(dis.dis('s[0] += lst'))
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, key=len, reverse=True))
fruits.sort() #Returns none, sorts inplace
print(fruits)
