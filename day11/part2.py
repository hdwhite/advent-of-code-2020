def seesoccupied(x, y, dx, dy):
    if dy == 0 and dx == 0: return False
    while True:
        x += dx
        y += dy
        if x < 0 or x >= len(seatlist[0]) or y < 0 or y >= len(seatlist): return False
        if seatlist[y][x] == "L": return False
        if seatlist[y][x] == "#": return True

with open('input') as f:
    newseatlist = f.read().splitlines()
newseatlist = list(map(list, newseatlist))

seatlist = []
while newseatlist != seatlist:
    seatlist = newseatlist
    newseatlist = []
    for i in range(len(seatlist)):
        newseatlist.append([])
        for j in range(len(seatlist[i])):
            occupiednear = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    occupiednear += seesoccupied(j, i, dx, dy)
            if seatlist[i][j] == ".": newseatlist[i].append(".")
            elif seatlist[i][j] == "L":
                if occupiednear == 0: newseatlist[i].append("#")
                else: newseatlist[i].append("L")
            else:
                if occupiednear < 5: newseatlist[i].append("#")
                else: newseatlist[i].append("L")
    print('\n'.join(list(map(lambda x:''.join(x), newseatlist))))
    print("")
print(sum(list(map(lambda x:x.count("#"), seatlist))))
