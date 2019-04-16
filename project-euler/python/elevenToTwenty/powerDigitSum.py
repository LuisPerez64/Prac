'''
Is given a number, and adds up the values, of each of it's individual integer 
points. Extremely easy with string manipulation.
'''
def addThemUp(inputString):
    total = 0
    for i in inputString:
        total += int(i)
        
    return total

inputVal = str(2**1000)
print(addThemUp(inputVal))
