'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five
then  there are 3+ 3 + 5 + 4+ 4 = 19 letters used in total.
If all the numbers in from 1 to 1000, inclusive were written out in words, how
many letters would be used?
'''
'''
@Params: 
 inputVal: The value to be pushed forward in the calculation.
 inputString: The string that is returned to the caller function.

@Returns: 
 The string that is to be aligned with the given key that is in the dict that
 is going to be used for this.

@Funct:
 Will use recursive calls to append the needed name of the given digit to the 
 list, and move from there forward.
'''
def populateDict(inputVal, inputString= None):
    if inputString == None:
        inputString = ''
        
    if inputVal < 20:
        tempString = {#Switch statement?
            0: '',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen'
        }[inputVal] #Should not call anything else past this
        return tempString #last point out.
    elif inputVal < 100: #Handler for values below 100
        temp = inputVal % 10
        inputVal -= temp
        tempString = { #Append, if needed, the values incremented by 10
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'
        }[inputVal]
        if temp != 0: #Add in or remove the hyphen from the output of the code
            tempString += '-'
            #Add the values within the 0-9 to the value placed here
        inputString += tempString + populateDict(temp, inputString)
        return inputString
    elif inputVal < 1000:
        temp = inputVal % 100
        tempTwo = inputVal //100 #Get the floor of the division
        tempString = populateDict(tempTwo) + ' hundred '
        if temp != 0: #To make sure pure hundreds are outlined well.
            #Only adds the and if the value % 100 is not zero
            tempString += ''
        inputString += tempString + populateDict(temp, inputString)
        return inputString
    elif inputVal < 10000:
        temp = inputVal % 1000
        tempTwo = inputVal // 1000
        tempString = populateDict(tempTwo) +' thousand '
        inputString += tempString + populateDict(temp, inputString)
        return inputString

#print("module.exports = {")
for i in range(1,100):
    inp = populateDict(i)
#    inp = inp.capitalize() #Capitalize the first letter in the string
    print("\""+inp+"\": [\n        \"NUM\"\n    ],")

#print("};")
