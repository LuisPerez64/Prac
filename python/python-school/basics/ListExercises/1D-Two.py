# Could be employed so much simpler with a map, but not needed.
print('Beginning list manipulation, in hopes to get the tv schedule for the station.')
try:
    input = raw_input
except:
    pass

stationsList = []
while True:
    station = input('What is the stations name (no input to exit): ')
    if station == '':
        break
    stationsWeek = []
    while True:
        dayOfWeek = input('What day of the week is it (no input to exit): ')
        if dayOfWeek == '':
            break
        stationShows = []
        while True:
            showName = input('Name of the show (no input to exit): ')
            if showName == '':
                break
            showTime = [input('{1}\'s {0} time: '.format(x, showName)) for x in ['start', 'stop']]
            stationShows.append((showName, showTime))
        stationsWeek.append((dayOfWeek, stationShows))
    stationsList.append((station, stationsWeek))

for ind in stationsList:
    print('Station: {0}'.format(ind[0]))
    for indK in ind[1]:
        print('\tDay of Week {0}.'.format(indK[0]))
        for indJ in indK[1]:
            print('\t\tShow Name: {0} Starts at {1} Ends at {2}'.format(indJ[0], indJ[1][0], indJ[1][1]))
