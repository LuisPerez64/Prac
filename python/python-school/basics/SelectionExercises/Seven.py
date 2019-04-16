months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
while True:
    userInp=[int(x) for x in input('Please input date in format yyyy mm dd ie 1982 10 08: ').split(' ') if x is not '']
    if userInp[1] > 12 or userInp[1] < 1:
        print('Sorry that\'s not a valid month.')
        continue
    if userInp[2] < 1 or userInp[2] > 31 or (userInp[1] == 2 and userInp[2] > 29):
        print('Sorry that is not a valid day for the given month.')
        continue
    break
print('It is {0} {1}, {2}'.format(months[userInp[1]-1]+'.', userInp[2], userInp[0]))



        
