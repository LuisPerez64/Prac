words = ['super', 'saiyan', 'octomom', 'random', 'saucy']

print('Words beginning with the letter \'s\':')
for word in words:
    if word[0] == 's':
        print(word)

print('Total words with the letter s, as the first letter {0}.'.format(len([x for x in words if x[0] == 's'])))
