a = 0b111111000110000000000000000110000000000
b = 0b111111000000000000000000000110110000000


index = [3,3,0,2,0,0,0,0,0,2,0,0,0]
colums = [3,3,0,0,0,0,0,0,0,2,2,0,0]
count = 3
index_str = ''
colums_str = ''
for i in index:
    for j in range(0,i):
        index_str+='1'
    for k in range(0,count - i):
        index_str+='0'
for i in colums:
    for j in range(0,i):
        colums_str += '1'
    for k in range(0,count - i):
        colums_str += '0'
print(index_str)

for i in range(0,len(index_str)):
    if index_str[i] != colums_str[i]:
        print(1)



def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

print(encode(e))
def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


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

