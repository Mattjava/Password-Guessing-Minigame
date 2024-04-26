import random

# Generates a random lowercase letter as a character.
def generateLetter():
    asciiNum = random.randint(97, 122)
    return chr(asciiNum)

# Generates a string using a given length and a random amount of characters.
def generateString(length):
    newStr = ""

    for i in range(length):
        newStr = newStr + generateLetter()

    return newStr
