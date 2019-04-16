### Iteration Exercises

##### Exercises meant to employ the basic iteration techniques that were learned throughout the past chapters.
#####  Introduction to [time](https://docs.python.org/3/library/time.html) module
##### Introduction to shifting. An assignment operator
###### Good usage with regards to Boolean Algebra
###### << (Right Shift. Effectively Divide by 2)
###### >> (Left Shift. Effectively Multiply by 2)
##### Going deeper into [format](https://docs.python.org/3/library/functions.html?highlight=format#format) text, with delimitations.
```python
inp=('I will fit','I will not fit')
print('''Different outputs:                                    
Width Delimiting {3} Fit's: '{0:10}' Doesn't: '{1:10}' Does: '{1:20}'
Left Alignment: {4} {0:<20}
Right Alignment: {5} {0:>20}
Center Alignment: {6} {0:^20}
Float Delimiting: {7} ie. {8} Val:{2} Format:{2:.2f}
'''.format(inp[0],inp[1],1234.567, '{0:width}', '{0:<width}',' {0:>width}','{0:^width}','{0:spacesBefore.spacesAfter(formatSpecifier)}','{0:.2f}' ))
```

#### Linear Search Algortihm Implementation
```python
# Item being searched for.
searchItem=4
# Populate a list with 100 values
inpList=range(100)

## Brute:
index=0
found=False
lengthOfList=len(inpList)
# Iterate through the list, incrementing the index as needed.
while not found and index < lengthOfList:
    if list[index] == searchItem:
        # Found the value that was being sought.
        found=True
    else:
        index+=1
print('Found element: {0} at index {1}.'.format(searchItem, index))

## Brute Pythonic
index=-1
# Added the enumerate to be able to index the location of the found variable. 
for ind,inp in enumerate(inpList):
    if inp == searchItem:
        index=ind
        break
print('{2} element: {0}, index {1},'.format(searchItem,index, 'Found' if index != -1 else 'Could not find'))

## Pythonic (Simpler one line easily readable.)
# Using next with a default value if searchItem not found. Caveat being, only one instance is dealt with.
index=next( (i for i,j in enumerate(inpList) if j == searchItem), -1)
print('{2} element: {0}, index {1},'.format(searchItem,index, 'Found' if index != -1 else 'Could not find'))

## Function wrapped for reusability
def findIndex(searchItem):
    index=next( (i for i,j in enumerate(inpList) if j == searchItem), -1)
    print('{2} element: {0}, index {1},'.format(searchItem,index, 'Found' if index != -1 else 'Could not find'))
```

#### Introductory String Slicing
    String slice formatting: [start:end:stepping]
    Lists, strings, most any type of construct can be sliced
```python
inp='I like python, like Monty so yeah'
print('''Original input: "{0}"
Trim first ten letters off "{1}"
Trim Last ten letters "{2}"
Trim first five, last 5 "{3}
Reversed "{4}"'''.format(inp,inp[10:],inp[:-10],inp[5:-5], inp[::-1]))

# Output:
'''
Original input: "I like python, like Monty so yeah"
Trim first ten letters off "hon, like Monty so yeah"
Trim Last ten letters "I like python, like Mon"
Trim first five, last 5 "e python, like Monty so"
Reversed "haey os ytnoM ekil ,nohtyp ekil I"
'''
```

#### Basic Exercises:
1. [x] Create a program that will ask the user for a number and then print out a list of number from 1 to the number entered and the square of the number.
2. [x] Create a program which will produce the times table for an number entered by the user.
3. [x] Write a program that will add together a series of numbers until the user enters a rogue value of 0. The program will then display the total.
4. [x] Create a program which will count down from 10 to 0, indicating how long there is to go before time runs outs. When time runs out it should display a suitable message.

#### (Hopefully) Challenging Exercises
1. [x] Create a program that uses linear search to check that a given character is in a given string.
2. [x] Extend the previous exercise so that it will display the string showing instances of the provided character and blank characters for the remaining letters. For example, if the string was "hello" and the user entered "l" the program would display " _ l l ".

#### (Hopefully) Very Challenging Exercises
1. [x] Create a program which will convert a given decimal up to 255 into its 8-bit binary equivalent.
2. [x] Extend the previous exercise to convert the binary number to hexadecimal.
3. [x] Create a program to convert from hexadecimal to decimal.

#### Difficult Exercises
1. [x] Extend (Hopefully) Challenging Exercise 2 so that it will allow you to check for another character (until a rogue value is entered) and displays an appropriate message based on the result. For instance, if you entered 'e' you would see " e l l _ " and if you entered 'm' you would see "m is not in " _ l l _".
2. [x] Improve the previous exercise so that it is a complete game of hangman for two players which gives a set number of guesses to the user and displays an appropriate message for the winner.