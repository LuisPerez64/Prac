def isSmallest(inputInt):
    for i in range(3,20):
        if inputInt % i != 0:
            return False
    return True

count = 20
while True:
    if isSmallest(count) == True:
        break
    count += 20

print count

''' 
I have no idea how this works and why it's so much better than what I did.
def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print i
'''
