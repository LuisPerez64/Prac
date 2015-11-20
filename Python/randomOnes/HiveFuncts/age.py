'''
Mainly just a practice point that tests a string, and evaluates wheter a person is speaking about someones age in itself.

'''

'''
Makes the string of letters into a list of Strings themselves.
'''
def makeList(inpString):
    word = ""
    retList = []
    #inpString+=" " #Acting pointless and not adding in the needed 99
    for i in inpString:
        print(i)
        if not i.isalnum():
            retList.extend([word])
            word = ""
        else:
            word += i

    return retList

'''
Simple sentence validation simulation.
Simple to make the properNoun hold multiple names of "Proper Nouns"
'''

def speakingOfAge(inpString):
    inpString = makeList(inpString) #Convert the sentence into a list of words
    print(inpString)
    if checkForAge(inpString):
        print("Well got here")
    return True

def checkForAge(inpString):
    properNoun = []
    hasNumber = False  
    toggle = True
    for word in inpString: #Sift through the words in the list itself
        print(word)
        if word[0].isupper() and toggle: #Catches "Proper" Nouns
            properNoun.append(word)
        else: #After the first name is found then Lowercase implies name done
            toggle = False
        if word.isdigit():
                hasNumber = True

    #Returns true if there was a proper noun found, and holds a number in it.
    return hasNumber and len(properNoun)


l = "Bill Newman is 99 years old."
l2= "Bill Newman shot 99 people."
l3= "Bill Newman, just Bill Newman"
if speakingOfAge(l):
    print("Well yeah")
if speakingOfAge(l2):
    print("Well no")
if speakingOfAge(l3):
    print("Well no")
print("Here")
