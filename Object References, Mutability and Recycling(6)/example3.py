charles = {'name': 'Charles L. Dodgson', 'born': 1832}
alex = {'name' : 'Charles L. Dodgson', 'born' : 1832 , 'age' : 55}
lewis = charles 

print(lewis is charles)

print(id(charles), id(lewis))
lewis['age'] = 55
print(lewis)
print(charles)

# The == operator compares the values of objects (the data they hold), while is compares their identities.
print(alex == charles) #True
print(alex is not charles) #True
