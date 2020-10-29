inpParams = ['first', 'second']
try:
    input = raw_input
except NameError:
    pass

inpTeams = [input('Name of {0} team: '.format(x)) for x in inpParams]
inpScores = [int(input('What did {0} score: '.format(x))) for x in inpParams]

# Abit convoluted, but easy to follow weirdly enough. Love/Hate Python sometimes...
print('''
So {0}
'''.format('it\'s a draw. 1 Point for each' if inpScores[0] == inpScores[
    1] else '{0} won. 3 Points for them in the standings'.format(
    inpTeams[0] if inpScores[0] > inpScores[1] else inpTeams[1])))
