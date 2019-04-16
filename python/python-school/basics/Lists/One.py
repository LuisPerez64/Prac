import itertools
inpList=[12, 23, 1, 10, 5, 16]

maxVal=inpList[0]
for x in inpList:
    if x > maxVal:
        maxVal=x
        
print('''
Python has a Max value function {0}
My list filtering with itertools accumulate {1}
Brute force method {2}
'''.format(max(inpList),[ x for x in itertools.accumulate(inpList, max)][-1], maxVal)) 
