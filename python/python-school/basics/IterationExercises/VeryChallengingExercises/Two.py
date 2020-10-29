'''
Conversion from decimal 0-255. To binary.
'''
print('Python already has a to binary function "bin"')
inputInt = int(input('Please input the value to be converted: '))
# A list of the possible Hex Values.
hexList = [str(x) for x in range(10)]
hexList += ['a', 'b', 'c', 'd', 'e', 'f']


def myBin(inputInt):
    outBin = ''
    while inputInt:
        outBin += '0' if inputInt % 2 == 0 else '1'
        inputInt >>= 1
    return outBin[::-1]


# Expects a hex of format 12=~1100=~C
def myHex(inputBin):
    # Reverse the input, to be able to analyze it straight forward
    inp = inputBin[::-1]
    # Verify that the value given is a mod four %able binary string.
    # Severely convoluted... If len % 4 is not 0 then add what is needed to make it so
    # Pads with zeroes
    inp += ('0' * ((0 if len(inp) % 4 == 0 else 4) - (len(inp) % 4)))
    outHex = ''
    # Four point jumps in the string being processed.
    for quad in range(0, len(inp), 4):
        val = inp[quad:quad + 4]
        hexVal = 0
        # Basic 
        for i in range(4):
            hexVal += 2 ** i * int(val[i])
        outHex += hexList[hexVal]
    return 'Ox' + outHex[::-1]


print('''Originally input value: {0}
Python bin function: {1}
My implementation: {2}
Python hex function: {3}
My hex implementation: {4}'''.format(inputInt, bin(inputInt), myBin(inputInt), hex(inputInt), myHex(myBin(inputInt))))
