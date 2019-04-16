'''
Find the sum of all the positive integers which cannot be written as the sum of
 two abundant numbers.
'''
def factors(inputVal, inputList = None):
    toggle = False
    if inputList == None:
        inputList = [] # list does not exist, or was not passed in
        toggle = True
    for i in range(1, int(inputVal / 2) + 1):
        if inputVal % i == 0:
            inputList.extend([i])

    if toggle:
        return inputList

abundant = []
perfect = []
deficient = []

for i in range(1, 1000):
    total = sum(factors(i))

    if total == i:
        perfect.extend([i])
    elif total < i:
        deficient.extend([i])
    else:
        abundant.extend([i])

sumTo = []
for i in abundant:
    for j in abundant:
        sumTo.extend([i+j])

tot = 0
for i in range(1000):
    if i not in sumTo:
       tot += i 
print(tot)
'''
print("Perfects: ", perfect)
print("Deficent: ", deficient)
print("Abundant: ", abundant)
'''
