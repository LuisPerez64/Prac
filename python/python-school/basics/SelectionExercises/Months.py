seasons = {'summer': ['Jun', 'Jul', 'Aug'],
           'winter': ['Jan', 'Feb', 'Dec'],
           'fall': ['Sep', 'Oct', 'Nov'],
           'spring': ['Mar', 'Apr', 'May']}
days30 = ['Apr', 'Jun', 'Sep', 'Nov']
daysLeap = ['Feb']
isLeapYear = False
year = int(input('What year is it(format yyyy): '))
if year % 4 is 0 and year % 100 is not 0:
    isLeapYear = True
month = input('What month is it: ')[:3].capitalize()
for k in seasons:
    if month in seasons[k]:
        print('That months in the {0}.'.format(k.capitalize()))
        print('This month has {0} days'.format(
            30 if month in days30 else 29 if (month in daysLeap and isLeapYear) else 28 if (
                        month in daysLeap and not isLeapYear) else 31))
