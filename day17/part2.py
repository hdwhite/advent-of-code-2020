def getneighbours(p):
    num = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if (i | j) | (k | l) == 0: continue
                    if (p[0]+i, p[1]+j, p[2]+k, p[3]+l) in grid: num += 1
    return num

with open('input') as f:
    startgrid = f.read().splitlines()

grid = set()
for i in range(len(startgrid)):
    for j in range(len(startgrid)):
        if startgrid[i][j] == "#": grid.add((i, j, 0, 0))

for i in range(6):
    print(grid)
    newgrid = set()
    for point in grid:
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    for w in [-1, 0, 1]:
                        testpoint = (point[0]+x, point[1]+y, point[2]+z, point[3]+w)
                        if getneighbours(testpoint) == 3:
                            newgrid.add(testpoint)
        if getneighbours(point) == 2:
            newgrid.add(point)
    grid = newgrid
print(newgrid)
print(len(newgrid))
