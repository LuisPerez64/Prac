num = float(input('Please inpu a value. Try and stay in the range 1 - 20 '))

print('The value {0} is {1}.'.format(num, 'too low' if num < 1 else 'too high' if num > 20 else 'just right'))
