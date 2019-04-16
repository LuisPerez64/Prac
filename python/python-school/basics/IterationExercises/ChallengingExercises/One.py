inpString=input('Input the string: ')
searchItem=input('What are you searching for: ')

index=next( (i for i,j in enumerate(inpString) if j == searchItem), -1)
print('{2} element: {0}, index {1}.'.format(searchItem,index, 'Found' if index != -1 else 'Could not find'))
