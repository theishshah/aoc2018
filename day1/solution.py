def freq():
    data = open("data.txt", "r")
    lines = data.readlines()
    score = 0
    for step in lines:
        score += int(step)
    return score

def repeat():
    seen = {}
    data = open("data.txt", "r")
    lines = data.readlines()
    score = 0
    while(1):
        for step in lines:
            score += int(step)
            seen[score] = seen.get(score, 0) + 1
            if seen[score] == 2:
                return score

print(repeat())
