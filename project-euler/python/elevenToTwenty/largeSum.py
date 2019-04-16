'''
Is given a file, with a bunch of very large numbers, and takes that and adds it
up, displaying the number.

The specifiedprogram only wants the first 10 digits of the given number.

File dependency: largeSum.txt
'''
#This may not be the smartest thing to do, dependencies should be local.
import sys
sys.path.append("../myPyFuncts") # Add the path to my functs to search
import readInFile #Holds the read functions

list = readInFile.readInFileOfNumbers("largeSum.txt")
sum = 0
for i in list:
    sum += i

#Convert the sum to a string
sum = str(sum)
print sum[0:10]

