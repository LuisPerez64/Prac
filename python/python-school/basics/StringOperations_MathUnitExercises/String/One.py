'''
String manipulation.
Output with different formats as needed.
'''
# Short work around for compatibility. This is by no means a great fix, but good to know
# Will add this to main readme.
try:
    input = raw_input
except NameError:
    pass

inpQuote = input('Please input the quote that you\'d like to manipulate:\n')
print("""
Original Quote:
"{4}"

Let's make it all upper case:
"{0}"

Lower now:
"{1}"

Capitalizing the first:
"{2}"

Title Casing:
"{3}"
""".format(inpQuote.upper(), inpQuote.lower(), inpQuote.capitalize(), inpQuote.title(), inpQuote))
