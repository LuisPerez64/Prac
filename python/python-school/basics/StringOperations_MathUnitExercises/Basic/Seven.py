# No Const in python, unless creating a one item tuple.
constRate = (0.92,)

print('Welcome to the conversion from Dollars to Euros, at current market 1 Dollar = {0} Euros'.format(constRate[0]))

moneys = float(input('How much money are we bringing with us American: '))

print('Wow with ${0} we\'d have about {1} Euros.'.format(round(moneys, 2), round(moneys * constRate[0], 2)))
euros = int(moneys * constRate[0])

print('''
Let me put this in some perspective that\'s {0} 50 Pound Note(s), {1} 20 Pound Note(s),{2} 10 Pound Note(s), and {3} 5 Pound Note(s), with {4} Pence left over,
'''.format(euros / 50, euros % 50 / 20, euros % 50 % 20 / 10, euros % 50 % 20 % 10 / 5,
           round(moneys * constRate[0], 2) % 50 % 20 % 10 % 5))
