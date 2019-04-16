inpLabels=['Motorway','Back Roads','Through Town']
inpSpeeds=(65,55,35)
print('''
If travelling by {0} speed limit is {1} MPH.
If travelling by {2} speed limit is {3} MPH.
If travelling {4} limit is {5} MPH.
'''.format(inpLabels[0],inpSpeeds[0],inpLabels[1],inpSpeeds[1],inpLabels[2],inpSpeeds[2])
)
while True:
    try:
        choice=input('''
So travelling by:
(0) Motorway
(1) Roadway
(2) Through Town
Choice: ''')
        choice=int(choice)
    except ValueError:
        print('Invalid choice {0}'.format(choice))
        continue
    if choice >=0 and choice <= 2:
        break

distance=float(input('What distance are you dealing with: '))

print('Travelling {0} miles, by {1}, it\'ll take you {2} hours to get there.'.format(distance,inpLabels[choice], round(distance/inpSpeeds[choice],2)))
