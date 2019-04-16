questions=['Is it on: ','Is there paper in the tray: ','Is there toner: ', 'Did you break it...:']
print('So you\'re having trouble with your printer? Let me help you with that.\nPlease answer yes(0) or no(1) for the questions asked.')

for i in questions:
    ans=int(input(i))
    if ans == 1:
        print('Wait for someone else to come along.')
        break

