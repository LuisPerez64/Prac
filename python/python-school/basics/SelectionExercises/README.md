## Summary 
Review of the skills that were learned from the Seciton so far.
#### Introduction to [all](https://docs.python.org/3.6/library/functions.html#all) and [any](https://docs.python.org/3.6/library/functions.html#any)
```python
inp=[0,0]
all([x == 0 for x in inp]) #True if all values equate to True
inp=[0,1]
any([x == 0 for x in inp]) #True if any of the values equate to True in input
```
#### Introduction to [enumerate](https://docs.python.org/3.6/library/functions.html#enumerate) 
##### An iterator, cannot be used alone, must be used within an iterator construct. Returns pairs of construct (0, 'a')
```python
inp=['a','b','c','d']
for i,j in enumerate(inp):
    print(i,j)
#Output:
'''
0 a
1 b
2 c
3 d
'''
```
#### Introduction to [next](https://docs.python.org/3.6/library/functions.html#next) 
##### A looping construct. Returns the next value that matches a given criterion. By itself returns the first value that matches the given condition, must be used in conjuction with an iterator. In conjnction with the enumerate module proves a simple manner of iteration, and indexing of a list. Appending a link to the next module page for Python 3.5+ due to need to research a bit more in depth. Find more uses, possibly useful in tree traversals, or hash traversal, to find if an element exists within it due to the fact that it stops as soon as an element is found, not as convoluted as for x in .... construct. 
```python
## Efficient manner of finding an element that matches a criterion.
inp=['a','b','c','d']
next(x for x in inp if x == 'c')
# Output:
'''
'c'
'''
next(i for i in range(15,0,-1) if i <5 and i>=3)
# Output
'''
4 # List is reversed so first element that matches is 4.
'''
## In conjunction with enumerate. Yields a good manner of indexing.
next(x for x,y in enumerate(inp) if y == 'c')
# Output:
'''
2 ###The index of the value c in the fiven input list.
'''
```
#### Exercises
1. [x] Extend exercise 5 from the previous set of additional exercises. As well as outputting how much volume remains in the lift, state whether the fridge would fit based on its dimensions. The program should tell you which dimension is the problem if it won't fit into the lift.
2. [x] Create a program which will ask the user for a distance and whether you will be travelling on Motorway, A-road or through town for the duration of travel. The program should output the minimum amount of time it will take to reach that distance.
3. [x] Ask the user to enter the current month, the program should output whether the month is in Winter, Spring, Summer or Autumn.
4. [x] Extend exercise 3 so that it will tell you the number of days in the given month (ignore leap years!).
5. [x] Create a program which will allow the user to enter the state of two switches (either 1 (on) or 0 (off)). The program should work out if both switches are on and then output the message 'the light is on'. Otherwise, the program should output the message 'the light is off'.
6. [x] Amend your program so that the program will switch the light on if eitherof the switches is on.
7. [x] Create a program which asks the user for 3 numbers representing the year, month and day e.g 1982 10 08 and then outputs in the form 8th October 1982.
8. [x] Create a program which will troubleshoot printing problems. The program should ask questions like 'is the printer turned on?' and 'is there paper in the printer'.
9. [xfg] Create a program which will ask for your recent exam score out of 60 and tell you what grade you got and how many more marks you would have needed to get the next grade up. You can decide on the grade boundaries yourself.
10. [x] Extend exercise 4 so that it takes into consideration leap years.