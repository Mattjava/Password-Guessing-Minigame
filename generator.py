import random

def generateLetter():
    asciiNum = random.randint(97, 122)
    return chr(asciiNum)

def generateString(length):
    newStr = ""

    for i in range(length):
        newStr = newStr + generateLetter()

    return newStr
