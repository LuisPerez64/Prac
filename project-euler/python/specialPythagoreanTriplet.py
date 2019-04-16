
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2+b^2==c^2
. This finds the pythagorean triplet for which a+b+c == Given number, 
'''
###
'''
Insanely brute force manner of checking for the given principle.
I have found many better solutions, but not too good at list comprehension to
try and call them my own as of yet. 
Plans to revisit these problems when better at the given language.
'''
def getProd(userInput):
    for a in range(1, ((userInput-1)/2)): #Can never go past userInput / 2
        for b in range(a+1, (userInput /2)): #Same as above
            for c in range(b+1, userInput+1):
                if a+b+c > userInput: break #Minor optimization
                if (a*a +  b*b == c*c):
                    if(a+b+c == userInput):
                        print a,b,c
                        return a*b*c
##                       

userInput = input('What number would you like to validate against: ')

print getProd(userInput)
