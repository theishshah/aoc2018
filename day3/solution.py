def overlap():
    data = open("data.txt", "r")
    lines = data.readlines()
    grid = [[0 for x in range(1000)] for y in range(1000)]
    count = 0
    for line in lines:
        id = int(line.split("@")[0].strip()[1:])
        x_start = int(line.split("@")[1].strip().split(',')[0])
        y_start = int(line.split("@")[1].strip().split(',')[1].split(":")[0])
        x_len = int(line.split("x")[0].strip().split(':')[1].strip())
        y_len = int(line.split("x")[1].strip())
        for x in range(x_start, x_start+x_len):
            for y in range(y_start, y_start+y_len):
                grid[x][y] += 1
                if grid[x][y] == 2:
                    count += 1
    return count

def noOverlap():
    data = open("data.txt", "r")
    lines = data.readlines()
    grid = [[0 for x in range(1000)] for y in range(1000)]

    for line in lines:
        id = int(line.split("@")[0].strip()[1:])
        x_start = int(line.split("@")[1].strip().split(',')[0])
        y_start = int(line.split("@")[1].strip().split(',')[1].split(":")[0])
        x_len = int(line.split("x")[0].strip().split(':')[1].strip())
        y_len = int(line.split("x")[1].strip())
        for x in range(x_start, x_start+x_len):
            for y in range(y_start, y_start+y_len):
                grid[x][y] += 1

    for line in lines:
        pure_claim = True
        id = int(line.split("@")[0].strip()[1:])
        x_start = int(line.split("@")[1].strip().split(',')[0])
        y_start = int(line.split("@")[1].strip().split(',')[1].split(":")[0])
        x_len = int(line.split("x")[0].strip().split(':')[1].strip())
        y_len = int(line.split("x")[1].strip())
        for x in range(x_start, x_start+x_len):
            for y in range(y_start, y_start+y_len):
                if grid[x][y] != 1:
                    pure_claim = False
        if pure_claim:
            return id

print(overlap())
print(noOverlap())
