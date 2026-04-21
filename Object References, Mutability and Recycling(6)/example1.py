# Example 6-1. Variables a and b hold references to the same list, not copies of the list

a = [1, 2, 3, 4]
b = a
a.append(99)
print(b) # 1 2 3 4 99
