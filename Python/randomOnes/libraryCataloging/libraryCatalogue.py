'''
Library cataloging Program

A small script to keep track of all of the Books that I 
currently have, and a count of any duplicates as well. Also houses the amount of
Books written by a certain author as well.
Want to make this my first Graphical Python Program.
''' 
import re #Regex management
catalogue=dict() #Key:Authors Name, Value: List Of Books
manipFile = "Catalogue.txt" # File to be read and written to
def main():
   
    readIntoDict(manipFile)
    print("Inputting a new value or searching the catalogue")
    print("(0) Quit \n(1) Input \n(2) Search\n")
    choice=input("Choice: ")

    if int(choice) == 1:
        newInput()
    elif int(choice) == 2:
        rudimentarySearch()
    else:
        exit()
    outputDict(manipFile)
'''
Reads in the needed file, and logs all of the lines into a list, one by one
Cleans up the end of each of the lists as well. Removing sole new lines as well
'''
def importFile(fileName, inputList = None):
    toggle = False
    if inputList is None:
        inputList = []
        toggle = True

    with open(fileName, 'r') as inputFile:
        inputList = inputFile.readlines()
    inputList = [x.strip('\n') for x in inputList]#if len(x) != 0 /Not working.
         
    if toggle: #Remove the total number of Bookspoint, and send it in.
        return inputList[:-1]

'''
Gets the catalogued files, and brings them back into the fold, so as to make
the catalogue expand as is needed, and when it is needed.

'''
def readIntoDict(fileName):
    inputList = importFile(fileName)
    newAuthorRegex = ".+: #.+\d" #Enforce a format operation
    authorNameRegex = '.+:'
    
    for line in inputList:
        q = re.search(newAuthorRegex, line)

        if q is not None: #New author found
            w = re.search('.+:', q.group(0))
            w = w.group(0).rstrip(':')
            catalogue[w] = []
        elif len(line) != 0:
            catalogue[w].extend([line])
'''
New data is being appended to the given dictionary, no duplicates.
'''
def newInput():
    print("Beginning input of the needed materials")
    while True:
        author=input("Input author name (~ to stop Input): ")
        if author == '~':
            break
        if author not in catalogue:
            catalogue[author] = [] #Append the new author
        while True:
            book=input("Book Name (~ to stop input): ")
            if book == '~': #Delimiter is met
                break
                if book not in catalogue[author]:
                    catalogue[author].extend([book]) #Add book to authors list
                else:
                    print(book," already exists in the library")
        
'''
Search function to be adapted when the time comes, and made graphical.
'''
def rudimentarySearch():
    query = input("What or Whom are you looking for: ")
    toggle = False
    
    #longmanner of doing this. Could use dict.items, but then it's sloppy...
    #Not enough material to make this be that efficient, will do so later on.
    for key in catalogue:
        if query == key: #Found the author that was getting seeked out.
            print("Author ",query," found.")
            showEm = input("Show all Books (Y/N): ")
            if showEm == 'y' or showEm == 'Y':
                toggle = True
            else:
                break

        for value in catalogue[key]:
            if query == value:
                print("Book ", query, " by author ", key," found")
                break #Found the book that was getting searched for
            if toggle: #If selected print out all books by the given author
                print(value)
        if toggle == True:
            break

'''
Output the contents of the updated Dictionary to the needed file.
'''
def outputDict(fileName):
    outString ='' #String stream object
    totalNumBooks = 0
    with open(fileName, 'w') as outFile:
        for i in sorted(catalogue):
            outString += i+ ": # of Books "+str(len(catalogue[i]))+'\n'
            for k in catalogue[i]:
                outString += k +'\n'
            outString+= '\n'
            totalNumBooks += len(catalogue[i])
        outString += '\n'+"Total Number of Books: " + str(totalNumBooks)
        outFile.write(outString)

if __name__ == '__main__':
    main()
