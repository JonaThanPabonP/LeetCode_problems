'''
Given two binary strings a and b, return their sum as a binary string.
'''

def addBinary(a: str, b: str) -> str:
    c = str(int(a) + int(b))
    sum = ''
    num = len(c)
    aux = 0
    for i in range(-1, -num-1, -1):
        if int(c[i])+aux == 0:
            sum = '0' + sum
            aux = 0
        elif int(c[i])+aux == 1:
            sum = '1' + sum
            aux = 0
        elif int(c[i])+aux == 2:
            sum = '0' + sum
            aux = 1
        elif int(c[i])+aux == 3:
            sum = '1' + sum
            aux = 1
    if aux == 1:
        sum = '1' + sum

    return sum


print(addBinary(a = "11", b = "1"))         # Output -> "100"

print(addBinary(a = "1010", b = "1011"))         # Output -> "10101"

print(addBinary(a = "1111", b = "1111"))         # Output -> "11110"