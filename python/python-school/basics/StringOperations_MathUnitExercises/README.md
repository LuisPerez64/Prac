ma## Summary
A short range of exercises that are meant to solidify the aspects learned in a few previous sections.
Introduced a few string operations, had not heard of string.(title|capitalize)
Introduced the math Module, with a slight introduction to 'import'
Interesting snippet(For when __future__ is not an option)
```python
try:
    input = raw_input
except NameError:
    pass
```
#### Basic Exercises
1. [x] Write a program that will ask the user for four integer numbers and then add these numbers together before displaying the answer. The input and output should be user friendly.
2. [x] Write a program that will ask the user for three integer numbers and then multiply the first two together before dividing the result by the third number. The input and output should be user friendly.
3. [x] Write a program that will ask the user for two numbers a then divide one by the other. The number of times one goes into another and the remainder should be displayed. For example, If 3 and 2 were entered: 3/2 = 1 remainder 1. The input and output should be user friendly.
4. [x] Improve the previous program to show only the integer part of the answer.
5. [x] Both a fridge and a lift have heights, widths and depths. Work out how much space is left in the lift once the fridge is inside. Assume that the fridge dimensions will fit. The input and output should be user friendly.
6. [x] Write a program that asks the user for the amount of money they will take on holiday and convert this into the equivalent amount in Euros, ignoring any Cents that might result from the conversion. The input and output should be user friendly.
7. [x] Improve the above program so that it will tell you how many 50,20,10 and 5 Euro notes you would receive for a given value of Pounds.

#### Math Unit Exercises
1. [x] Calculate the circumference and area of a circle when the user enters a radius. Round the answers to 2 decimal places. The input and output should be user friendly.
2. [x] A circular swimming pool is x metres in diameter. What volume of water does it contain if the pool is the same depth at all points?
3. [x] A plane is travels 20km on a course heading 60 degrees from north. Write a program that will calculate how far north and how far east has the plane travelled at this point?(Called Pythagoreas.py)
4. [x] Generalise the previous program so that it will work for any distance entered and degrees from north.(Done in 3)
5. [x] A road is inclined at an angle of 1 degree to the horizontal. Find the vertical height climbed when a car travels 1 km up the hill.(Done in 3)
6. [x] The foot of a ladder is 1.5m from a vertical wall. The ladder makes an angle of 68 degrees with the horizontal. How far up the wall does the ladder reach?(Done in 3)
7. [x] The string of a balloon is 120m long and makes an angle of 70 degrees with the horizontal. What is the height of the balloon.(Done in 3)

#### String Operation Exercises
1. [x] Create a program that will allow the user to enter a quote by a famous person. Output this quote in upper case, lower case, capitalise and title formats.
2. [x] Improve the program so that the user can replace a one word with another word.
3. [x] Improve the program so that the user can print out only part of the quote.
