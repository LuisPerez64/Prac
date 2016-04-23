'''
Do out the sorting algorithms, and make them make more sense
Try and do them as well as could be done for the gien language points.

Compare my implementation to the sort algorithms, provided by python3.* base 
'''
import random
def insertionSort(inputList):
    print("Placehold")

def mergeSort(inputList, start, end):
    if start < end:
        q = (start + end) // 2
        mergeSort(inputList, start, q)
        mergeSort(inputList, q+1, end)
        #merge(inputList, p, q, r)
        if len(inputList) >1:
            print(inputList[start:end])    

inpList = [60,12,27,5,46]#[ int(random.random() *100) for x in range(13) ]
print(inpList, "\nMerge it")

mergeSort(inpList, 0, len(inpList))







