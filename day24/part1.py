with open('input') as f:
    dirlist = f.read().splitlines()

blacktiles = set()
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
    print(len(blacktiles), coords)

print(len(blacktiles))
