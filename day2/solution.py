def checkTwo(line):
    letters = {}
    for c in line:
        letters[c] = letters.get(c, 0) + 1
    for key, val in letters.items():
        if val == 2:
            return True
    return False

def checkThree(line):
    letters = {}
    for c in line:
        letters[c] = letters.get(c, 0) + 1
    for key, val in letters.items():
        if val == 3:
            return True
    return False

def checksum():
    data = open("data.txt", "r")
    lines = data.readlines()
    twos = 0
    threes = 0
    for line in lines:
        twos += int(checkTwo(line))
        threes += int(checkThree(line))
    
    return twos*threes

def charMissing():
    data = open("data.txt", "r")
    lines = data.readlines()
    for box1 in lines:
        for box2 in lines:
            if len(box1) == len(box2):
                result = ""
                for i in range(0,len(box1)):
                    if box1[i] == box2[i]:
                        result += box1[i]
                if len(result) == len(box1)-1:
                    return result

print(charMissing())
