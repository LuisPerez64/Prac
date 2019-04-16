limit=int(input('Please input the last value to be evaluated: '))

for i in range(1,limit+1):
    print('{0} squared is {1}'.format(i, i**2))
