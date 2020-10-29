from bubbleSort import *

print('Welcome to your Shopping List. \nInput items until you are finished, then enter with no input to finish up.')

shoppingList = []
while True:
    item = input('What do you want to add: ')
    if item == '':
        break
    shoppingList.append(item)

bubbleSort(shoppingList)

for i, j in enumerate(shoppingList):
    print('Item {0}: {1}'.format(i, j))
