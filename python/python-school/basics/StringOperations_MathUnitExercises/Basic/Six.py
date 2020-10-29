# No Const in python, unless creating a one item tuple.
constRate = (0.92,)

print('Welcome to the conversion from Dollars to Euros, at current market 1 Dollar = {0} Euros'.format(constRate[0]))

moneys = float(input('How much money are we bringing with us American: '))

print('Wow with ${0} we\'d have about {1} Euros.'.format(round(moneys, 2), round(moneys * constRate[0], 2)))
