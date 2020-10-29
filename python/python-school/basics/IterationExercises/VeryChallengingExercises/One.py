'''
Conversion from decimal 0-255. To binary.
'''
print('Python already has a to binary function "bin"')
inputInt = int(input('Please input the value to be converted: '))


def myBin(inputInt):
    outBin = ''
    while inputInt:
        outBin += '0' if inputInt % 2 == 0 else '1'
        inputInt >>= 1

    return outBin[::-1]


print(''' Originally input value: {0}
Python bin function: {1}
My implementation: {2}'''.format(inputInt, bin(inputInt), myBin(inputInt)))
