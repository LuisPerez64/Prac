'''
Wrapping in a class prior to moving to MyImplementations
Implementations of the linear search algorithm. 
Brute force. No python enhancements, the way it would be written in some other languages
Pythonic Brute. A bit of python secret sauce added, still at heart the brute force
Pythonic. Using the constructs fully provided to find the given element in the input
Will all take three paramenters:
   List being traversed
   Item being searched for
   Optional begin from, used if multiple elements are being sought, and within the caller in a loop 
All return either -1 if not found or index of item in the list
'''
# Straight forward brute method. Easy to read through, recognizeable
def brute(inpList, item, beginFrom=0):
    index=beginFrom
    found=False
    lengthOfList=(len(inpList))
    # Iterate through the list, incrementing the index as needed.
    while not found and index < lengthOfList:
        if list[index] == item:
            # Found the value that was being sought.
            found=True
            break
        else:
            index+=1
    if not found:
        index=-1
    return index


# Pythonic brute force method. If familiar with the language simple to read through.
# Cuts down the maount of lines needed considerably from normal brute
def brutePy(inpList, item, beginFrom=0):
    index=-1
    # Makes use of the enumerate iterator to assign an index to each list element
    for ind,inp in enumerate(inpList[beginFrom:]):
        # inp holds the current value at the ind point of the list 
        if inp == item:
            index=ind
            break
    return index

# Pythonic
def pythonic(inpList, item, beginFrom=0):
    #Using next. Somewhat cheating, as next in itself is a search algorithm
    # Warp it in next, get the indexes from enumeration
    # If the items match at any point return index, else return -1
    return next( (ind for ind,inp in enumerate(inpList[beginFrom:]) if inp == item), -1)
    
# Adds an item to the list if it's not already in it. Somewhat set-like, but only if used from start
def addIfNotIn(inpList, item):
    index=pythonic(inpList, item)
    # if the element is not in the list, add it. Make the index last element
    if index == -1:
        print('Element not in list. Appending: {0}'.format(item))
        inpList.append(item)
        index=len(inpList)-1
        
    return index

# Find all instances of a given item. Return them as a list   
def findAll(inpList, item):
    inst=[]
    ind=0
    while True:
        # Consistently log the index of the last found variable, if -1 no more, so break
        ind=pythonic(inpList, item, ind)
        if ind == -1:
            break
        inst.append(ind)
    return inst
