'''
Intro to all. If all equate to true then true, else false
'''
inputs=[int(input('Is light {0} on(1) or off(0): '.format(x))) for x in ['one', 'two']]
print('Light is {0}'.format('On' if all([x == 1 for x in inputs]) else 'Off'))
