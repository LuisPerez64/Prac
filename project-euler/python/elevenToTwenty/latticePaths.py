'''
Dictionaries cannot use lists, as keys. Just use 
'''
'''
Recursvie manner of implementing this, can be done with the choose.
This is a weird manner of doing this to me, under the guise of ininite allocation space. 
Solution with the combinatorial manner is done in the C++ version of this.

Explanation:
  Go through the list, One path is found when it is no longer possible to go 
  from one x,y pair. Amasses all possible paths from each of the x,y pairs.
  The last x,y pair that is ammassed is the 20,20 which is the one that is 
  returned. Interesting concept.
'''
def gridSize(xAxis, yAxis, dictOfVars):
    if xAxis == 0 or yAxis == 0: # one path is found, when no more possible
        return 1 # Reached the end of the possible paths, for this pair.
    if (xAxis, yAxis) in dictOfVars:
        return dictOfVars[(xAxis,yAxis)] #The tuple is in the dict, return it
    
    #At every point populate the hastable.
    dictOfVars[(xAxis, yAxis)]= (gridSize(xAxis-1, yAxis,dictOfVars) + 
                                 gridSize(xAxis, yAxis-1, dictOfVars))
    return dictOfVars[(xAxis, yAxis)]

#Create them empty dict:
#Keys, Tuples (xAxis,yAxis), Values: Length of the path from that tuple point.
dictOf = dict()
print(gridSize(20,20, dictOf))
print(dictOf)
