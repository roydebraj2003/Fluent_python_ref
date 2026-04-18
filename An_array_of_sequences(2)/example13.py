invoice = """
0.....6.................................40........52...55........
1909    Pimoroni PiBrella                 $17.50     3     $52.50
1489    6mm Tactile Switch x20            $4.95      2     $9.90
1510    Panavise Jr. - PV-201             $28.00     1     $28.00
1601 PiTFT Mini Kit 320x240               $34.95     1     $34.95
"""

SKU = slice(0, 6) #slice(start, end, step) slice object for reusability

DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
TOTAL= slice(55, None)

ITEMS_LIST = invoice.split('\n')[2:]

for item in ITEMS_LIST:
    print(f'{item[UNIT_PRICE]} {item[DESCRIPTION]}')


class Demo:
    def __getitem__(self, key):
        print(key)

d = Demo()
print(d[1:5, 2:8])
