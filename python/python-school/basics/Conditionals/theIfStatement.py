age=int(input('How old are you: '))

if age < 18:
    print("You are not yet old enough to vote.")
else:
    print("Wow you're all grown up. Go out and vote.")

print("By the way you {0}".format( 'retired already right?' if age>65 else 'can retire in {0} years.'.format(65-age)))
