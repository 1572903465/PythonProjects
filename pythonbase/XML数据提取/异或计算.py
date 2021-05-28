a = 0b111111000110000000000000000110000000000
b = 0b111111000000000000000000000110110000000


def BinToDec(value):
    try:
        return int(value, 2)
    except ValueError:
        return "Invalid binary Value"
# a = 0b100
# b = 0b111
c = a^b
print(bin(a))
print(bin(a^b))

while c>0:
    i = c%2
    c = int(c / 2)
    if i == 1:
        print(i,bin(c))

