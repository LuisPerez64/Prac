''' 
This program is given a rather large integer, and from that integer forms the 
product, of a given size of the seperate integers, adjacently that it could 
find and relays them to the user
'''
###
'''
@Params:
  inputList: The large int, placed in a list for convenience.
  startFrom: The index in the list to begin reading from, update each iter.
  readThisMuch: How much of the list to read in, user specified length.

@Returns:
  -1: If the list would go out of bounds from this rangecheck break, send EOF
  any+Int: The product within the gien range to the user.

#Note: May be deprecated.
This is more or less a dummy function. It does not do range checking.
It seems more adequate to have the caller function do that. Adding it anyways..
'''
def findProdInRange(inputList, startFrom, readThisMuch):
   returnProd = 1
   #This is the bounds checking function. If this is ever met, then the next
   #value to be read in would break the list, so send signal quit
   if readThisMuch + startFrom  > len(inputList):
      return (-1)
   #Remember the range functionalities, and how they affect the for loop
   for i in range(readThisMuch):
      returnProd *= int(inputList[startFrom + i])
 
   return returnProd

##  
largeInt = open("longInt.txt", "r")
if largeInt.closed == True:
   print 'That file does not exist. Exiting.'
   exit

#Read the contents from the opened file, copy into a new object to house them.
fileConts = largeInt.read()
newFile =[]
for i in fileConts:
   if i != '\n':
      newFile.extend([i])

#Close what you open up, don't fuck things up
largeInt.close()

rangeCheck = raw_input('Range to check in the int: ') # the amount of nums read
rangeCheck = int(RangeCheck) # Assign once here to the needed type.
startFrom = 0 # Range for the needed point of multiplying forwards

printVal = 0
retVal = 0
# The two statements are equivalent, one lets the function handle EOF
while retVal != -1: #(int(rangeCheck) + startFrom) <= len(newFile): 
   retVal = findProdInRange(newFile, startFrom, rangeCheck)
   if retVal > printVal:
      printVal = retVal
   startFrom +=1

print printVal
