### Introductory Conditional statements. Getting started
Began with the if statement. Came accross Pythons Ternary operator, not as it is in most languages ie
```C++
...
int x = 0;
int y = (x == 0 ? 12 : 15)
...
//Format condition ? if True : if False
```
Python's implementation is:
```python
...
x = 0
y = 12 if x == 0 else 15
...
#Format (condition)True if conditionCheck else (condition)False 
```

#### Exercises
1. [x] Write a function that asks the user how old they are. Tell them if they are old enough to vote. Then extend the program tell them how many years it is until they can retire (assume at age 65).
2. [x] Write a function that asks the user to input a number between 1 and 20. Give a response which indicates if the number is either within the range, too high or too low.
3. [x] Write a function which inputs the names of two football teams, and the score of one team followed by the score of the other team. Your function should calculate how many points each team gets (3 for a win,1 for a draw, 0 if they lose).