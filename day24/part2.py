def getneighbours(x, y):
    num = 0
    for i, j in nearby:
        num += (x+i, y+j) in blacktiles
    return num

with open('input') as f:
    dirlist = f.read().splitlines()

blacktiles = set()
nearby = [(-1, -1), (-1, 0), (0, -1), (0, +1), (1, 0), (1, 1)]
for curtile in dirlist:
    coords = [0, 0]
    hold = None
    for curchar in curtile:
        if curchar == 'n' or curchar == 's':
            hold = curchar
        else:
            if hold is None:
                if curchar == 'e': coords[1] += 1
                else: coords[1] -= 1
            elif hold == 'n':
                coords[0] -= 1
                if curchar == 'w': coords[1] -= 1
            else:
                coords[0] += 1
                if curchar == 'e': coords[1] += 1
            hold = None
    coords = tuple(coords)
    if coords in blacktiles: blacktiles.remove(coords)
    else: blacktiles.add(coords)

for i in range(100):
    newpattern = set()
    for curtile in blacktiles:
        if getneighbours(*curtile) == 1 or getneighbours(*curtile) == 2:
            newpattern.add(curtile)
        for i, j in nearby:
            if getneighbours(curtile[0]+i, curtile[1]+j) == 2:
                newpattern.add((curtile[0]+i, curtile[1]+j))
    blacktiles = newpattern
    print(len(blacktiles))
