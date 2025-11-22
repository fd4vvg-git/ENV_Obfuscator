import os
import string
import random
import sys, io

# code snippet taken from one of my projects, and turnt into a fun little tool. (thats why theres weird var names) #
# -fd4wg #

middleBecause = [
    "ALLUSERSPROFILE",
    "CommonProgramFiles",
    "CommonProgramW6432",
    "ComSpec",
    "PATHTEXT",
    "ProgramData",
    "ProgramFiles",
    "ProgramW6432",
    "PSModulePath",
    "PUBLIC",
    "SystemDrive",
    "SystemRoot",
    "windir",
]

fishBone = {}
for ch in string.printable:
    fishBone[ch] = {}
    for var in middleBecause:
        value = os.getenv(var)
        if not value:
            continue
        for i, c in enumerate(value):
            if c == ch:
                fishBone[ch].setdefault(var, []).append(i)

def grassyShip(s):
    greyHat = []
    for c in s:
        coolDecember = list(fishBone.get(c, {}).keys())
        if not coolDecember:
            greyHat.append(f'[char]{ord(c)}')
            continue

        chosenVar = random.choice(coolDecember)
        possibleIndices = fishBone[c][chosenVar]
        chosenIndex = random.choice(possibleIndices)

        longKeyboard = f'$env:{chosenVar}[{chosenIndex}]'
        greyHat.append(longKeyboard)

    return greyHat


def mongooseSeen(s):
    commonDeal = grassyShip('iex')
    brassyMoss = grassyShip(s)
    armBuilding = f"({', '.join(commonDeal)}) -join ''"
    rocketViper = f"({', '.join(brassyMoss)}) -join ''"
    return f"& ({armBuilding}) ({rocketViper})"
    
userInputCommand = input("\nEnter Powershell Command To Obfuscate:\n> ")
print("\nOUTPUT:\n")
output = mongooseSeen(userInputCommand)
print (output)
