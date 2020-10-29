'''
User inputs four integers. The sum of the integers is then returned to them.
With the use of list comprehension. The lessons are worth running through but 
super tedious, lest the basics will be.
'''

print("Please input four numbers.")
inpList = [int(input('Input number {0}: '.format(x + 1))) for x in range(4)]
print('Sum of these values is {0}'.format(sum(inpList)))
