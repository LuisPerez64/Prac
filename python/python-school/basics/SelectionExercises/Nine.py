'''
Grade scale is >59 ~ S, 50-58 ~ A, 40-50 ~ B,30-40 ~ C, 20-30 ~ D, <20 ~ F
'''
gradesList = [58, 50, 40, 30, 20, 0]
letterGrade = ['S', 'A', 'B', 'C', 'D', 'F']
curGrade = float(input('What grade did you get for your last Quiz: '))

letter = [0 if curGrade < x else 1 for x in gradesList]
# Introduced the next and enumerate modules.
# Next: Find the next item from the iterator that would have been called.
## Look into this function as I don't really understand it atm.
# Enumerate. Basic enumeration of the items contained in a list.
## When used in combination with next, as below will return the index of the
## value that matches the value that is being sought out by next.
ind = next((i for i, x in enumerate(letter) if x == 1))

print('You got a(n) {0} which is a(n) {1} . {2}'.format(round(curGrade / 60, 2), letterGrade[ind],
                                                        'Wow. Can\'t really get better than that can we. Congratulations.' if ind == 0 else 'We can always strive for a little bit more can\'t we. You\'d need {0} points to boost your score to a(n) {1}'.format(
                                                            gradesList[ind - 1] - curGrade, letterGrade[ind - 1])))
