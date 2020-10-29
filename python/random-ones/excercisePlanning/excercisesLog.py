import re  # Regex library

# Key:Muscle Worked Out, Value: Dict(Key:Equipment, Value:List Of Workouts)
excerciseDict = dict()
'''
Output Format:
Muscle Worked Out [
Equipment Used: # Of Excercises
Workout A
Workout B

Equipment Used: # Of Excercises
.
.
.
]

.
.
.

'''
excerciseDict = {'Chest': {'Bar': 'asd', 'Dumb': 'ssd'}, 'Ches': {'Low': 'asd', 'Prop': 'ssd'}}


def writeToFile(fileName):
    outputString = str()
    for key in sorted(excerciseDict):
        outputString += str(key) + " [\n"
        for subKey in excerciseDict[key]:
            outputString += (str(subKey) + ": # Of Excercises " +
                             str(len(excerciseDict[key][subKey])) + '\n')
            for workout in excerciseDict[key][subKey]:
                outputString += str(workout) + '\n'
            outputString += ']\n'
    with open(fileName, 'w') as outFile:
        outFile.write(outputString)


'''
Reads to excerciseDict
KeyRegex: .+(?=\[)
subKeyRegex: [A-z](?=: #)
workOutRegex: [A-z ]{2,} // If this is None, WorkoutInput Complete
'''


def readFromFile(fileName):
    keyRegex, key = '.+(?=\[)', ''
    subKeyRegex, subKey = '[A-z]+(?: #)', ''
    workOutRegex, workOut = '[A-z ]{2,}', ''
    with open(fileName, 'r') as inFile:
        for i in inFile:
            line = inFile.readline().strip('\n')
            if line == ']' or line == '':
                continue
            q = re.search(keyRegex, line)
            print(q)
            if q is not None:
                key = q.group(0)
                excerciseDict[key] = {}
            else:
                w = re.search(subKeyRegex, line)
                if w is not None:
                    subKey = w.group(0)
                    excerciseDict[key][subKey] = []
                    continue
                print(key, '\n', subKey, '\n', line)
                excerciseDict[key][subKey].extend([line])


if __name__ == "__main__":
    writeToFile("/tmp/test.txt")
    readFromFile("/tmp/test.txt")


def readFileToList(filename, outputIt=None):
    if outputIt == None:
        outputIt = False
    outputList = list()
    with open(filename, 'r') as inputFile:
        for line in inputFile:
            line = line.strip('\n')
            if (line == ''):
                continue
            outputList.append(line)
    if outputIt:
        printOutList(outputList)
    return outputList


def printOutDict(inputDict):
    for i in sorted(inputDict):
        print(i)
        if (type(inputDict[i]) == dict):  # To handle multiDicts
            printOutDict(inputDict[i])
        elif type(inputDict[i]) == tuple or type(inputDict[i]) == list:
            printOutList(inputDict[i])


def printOutList(inputList):
    for i in sorted(inputList):
        print(i)
