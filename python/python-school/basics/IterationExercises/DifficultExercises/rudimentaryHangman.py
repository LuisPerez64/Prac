'''
Rudimentary hangman. To be played by two people.
'''
import subprocess


def findInstances(inpString, searchItem):
    outList = []
    for ind, inp in enumerate(inpString):
        if inp == searchItem:
            outList.append(ind)
    return outList


with open('\dev\null', 'w') as NullPath:
    inpString = input('Input the word to be guessed: ')
    # Brought this in to make things a bit cleaner. Clear the screen right after input.
    subprocess.call('reset', stdout=NullPath)
    outString = ['_' for i in range(len(inpString))]
    # Six guesses
    count = 0
    while True:
        toggle = False
        inpSearch = input('What character are you guessing: ')
        inst = findInstances(inpString, inpSearch)
        for i in range(len(inpString)):
            if i in inst:
                outString[i] = inpString[i]
                toggle = True
        for x in outString:
            print(x, end='')
        print()

        if all(x != '_' for x in outString):
            print('Congratulations. You\'ve won.')
            break
        if not toggle:
            count += 1
        if count == 5:
            break
    if any(x == '_' for x in outString):
        print("Oooh! All right, that's it! Dishonor! Dishonor on your whole family!\n\
Make a note of this: dishonor on you, dishonor on your cow, dis...")
