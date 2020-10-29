# Rewrite this in JS, and find where the file pushes things back
import re

shortcuts = dict()


def makeShortcut(inputSentence):
    # No spaces in the shortcuts...
    q = re.findall("\[[A-z0-9]+:[A-z 0-9]+\]", inputSentence)
    if q is not None:  # Found a new shortcut brought in
        for i in q:
            l = i[1:-1]
            l = l.split(':')
            if l[0] not in shortcuts:
                shortcuts[l[0]] = l[1]  # Add it to the map
            inputSentence = inputSentence.replace(i, shortcuts[l[0]])  # Remove the old shortcut
    # Just in case the shortcuts are being brought in push them
    return outputShortcut(inputSentence)


def outputShortcut(inputSentence):
    for i in shortcuts:
        # Do nothing if the user escapes the
        newRe = r'(?<!\\)' + i
        # If not being escaped then replace
        inputSentence = re.sub(newRe, shortcuts[i], inputSentence)
        # Find the escaped points in the sentence
        newRe = r'\\' + i
        print(newRe, i)
        inputSentence = re.sub(newRe, i, inputSentence)  # For the escaped ones
    return inputSentence


inp = "Love how this could work [LP:Luis Perez] [KK:Crazy Hitler Loving Bastards] Blam boom \SS [SS:Schutzstaffel] [GG:Gestapo]"
print("Original:\n", inp, "\n\n")
print("New One:\n", makeShortcut(inp), "\n\n")

# Plans to build a semi common database for each topic, populated by users.
inp = "The SS known as the \SS were a bunch of KK. The SS were responsible for many of the most atrocious acts of the given time, and were regarded widely as hitlers secret military force. I don't actually know much about this, so for sport \GG are the GG as well."
"Simple regex replacement by LP  expanding in the futures."

print(outputShortcut(inp))
