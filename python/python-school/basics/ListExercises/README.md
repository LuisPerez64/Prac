# List Exercises
## Consolidation of the lessons that shoudl have been learned, and applications in the realm of list manipulations.

### Introduction to the Bubble Sort Algorithm 
###### Bubble sort is one of the rudimentary sorting algorithms. Brings forward the lowest/highest element in a given list, and moves it to the needed location. Then does this until all elements are in place.
###### Bubble Sort Implementation
```python
# Order a list from smallest to largest value.
noMoreSwaps=False
inpList=[x for x in range(100,0,-1)]
print('Unsorted list: {0}'.format(inpList))
while noMoreSwaps == False:
    noMoreSwaps=True
    for ind in range(len(inpList)-1):
        # Largest element in the list bubbles up to the top
        # swapping along the way
        if inpList[ind] > inpList[ind+1]:
            noMoreSwaps=False
            tempElement=inpList[ind]
            inpList[ind]=inpList[ind+1]
            inpList[ind+1]=tempElement
print('Sorted list: {0}'.format(inpList))
# Output
'''
Unsorted list: [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Sorted list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

'''
```
## 1D List Exercises
1. [x] Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.
2. [x] Write a program that will store the schedule for a given day for a particular TV station. The program should ask you for the name of the station and the day of the week before asking you for the name of each show and the start and stop times. Once the schedule is complete it should be displayed as a table.
3. [x] Create another version of the Hangman game, this time using Lists. The program should ask for the word to guess and the number of chances to be given. It should then split the characters in the word into individual items in a list. The other player should then be allowed to guess characters in the word. The program should display correctly guessed characters and unknown characters in the same way as the previous Hangman game. (Handled in the hangman.py)

## IE (Improvement Exercisese)
1. [x] Improve 1D List exercise 1 using a bubble sort so that the list is displayed in alphabetical order.
2. [x] Improve 1D List exercise 2 using a 2D List i.e. each show should have its own list containing the name of the show, start time and stop time.

## Very Challenging Exercises
1. [x] Create a game of Connect 4 for two players. Assume that there can only be vertical and horizontal wins. Diagonals are not allow for the moment. Ignore any validation of moves - assume no cheating!

## Noteable code slices.
###### Matrix manipulation, within the ConnectFour.py program. 
```python                                                                
# Convert the vertical slices to a list of lists. Easier to manipulate    
# Since it was not an n*n array, no simple way to rotate without manipulating the points that would be indexed. 
    # Pythonic Way         
    vertGrid=[[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
    for i in vertGrid:
        # Take the lists individually, convert to a string, try and find 4 in a row                  
        inp=''.join(i).find(symbol*4)
        if inp != -1:
            winner=True
    
    # Brute force
    for hori in grid:
        horiFirst=hori[0]
        horiCount=0
        for x in hori[1:]:
            if x == horiFirst and x is not '*':
                horiCount+=1
            else:
                horiCount=0
                horiFirst=x
            if horiCount == 3:
                winner=True
                indCount=0
                break
        if winner:
            break
    return winner
```