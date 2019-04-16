limit=int(input('Please input the last value for the times table.'))

for i in range(1,limit+1):
    for j in range(1,limit+1):
        print('{:^5}'.format(i*j), end='')
    print()
