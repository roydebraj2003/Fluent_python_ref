colors = ['Black', 'White']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors
                         for size in sizes]

for color in colors:
    for size in sizes:
        print(f'({color, size})')

print(tshirts)
