inpList=[23,44,551,12,3,5,5,6621]

sumTotal=0
totalEntries=0
for i in inpList:
    totalEntries+=1
    sumTotal+=i

print('For the list input, the total is {0}, with {1} entries, average is {2}'.format(sumTotal, totalEntries, sumTotal/totalEntries))

print('Simpler manner, with built in functions.')

print('For the list input, the total is {0}, with {1} entries, average is {2}'.format(sum(inpList), len(inpList), sum(inpList)/len(inpList)))
