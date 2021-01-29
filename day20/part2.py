def reversebits(n):
    result = 0
    for i in range(10):
        result = result << 1 | (n & 1)
        n = n >> 1
    return result

def findmonster(i, j, flip, rotate):
    monster = ["                  # ", "#    ##    ##    ###"," #  #  #  #  #  #   "]
    if flip: monster = monster[::-1]
    for x in range(rotate):
        newmon = [""]*len(monster[0])
        for y in range(len(monster[0])):
            for z in range(len(monster)):
                newmon[y] += monster[-1-z][y]
        monster = newmon

    if i + len(monster) >= len(stringgrid): return False
    if j + len(monster[0]) >= len(stringgrid[0]): return False
    subgrid = [x[j:j+len(monster[0])] for x in stringgrid[i:i+len(monster)]]
    
    for x in range(len(monster)):
        for y in range(len(monster[x])):
            if monster[x][y] == "#" and subgrid[x][y] != "#":
                return False
    print(i, j) 
    for x in range(len(monster)):
        for y in range(len(monster[x])):
            if monster[x][y] == "#":
                stringgrid[i+x] = stringgrid[i+x][:j+y] + "0" + stringgrid[i+x][j+y+1:]
    return True

class Tile:
    def __init__(self, tilenum, tiledata):
        self.contents = [i[1:-1] for i in tiledata[1:-1]]
        self.edges = [0, 0, 0, 0]
        self.neighbours = [None, None, None, None]
        self.tilenum = tilenum
        for curchar in tiledata[0]: self.edges[0] = (self.edges[0] << 1) | (curchar == "#")
        for curchar in tiledata: self.edges[1] = (self.edges[1] << 1) | (curchar[-1] == "#")
        for curchar in reversed(tiledata[-1]): self.edges[2] = (self.edges[2] << 1) | (curchar == "#")
        for curchar in reversed(tiledata): self.edges[3] = (self.edges[3] << 1) | (curchar[0] == "#")

    def addneighbours(self, matchlist):
        self.neighbours = matchlist

    def iscorner(self):
        for i in range(4):
            if self.neighbours[i] is None and self.neighbours[i-1] is None:
                return i
        return None

    def rotate(self):
        newgrid = [""]*len(self.contents)
        for i in range(len(self.contents)):
            for j in range(len(self.contents[0])):
                newgrid[i] += self.contents[-1-j][i]
        self.contents = newgrid
        self.edges.insert(0, self.edges.pop())
        self.neighbours.insert(0, self.neighbours.pop())

    def flip(self, edge):
        if edge % 2 == 0:
            self.contents = [i[::-1] for i in self.contents]
            self.edges = [reversebits(self.edges[0]), reversebits(self.edges[3]), reversebits(self.edges[2]), reversebits(self.edges[1])]
            self.neighbours = [self.neighbours[0], self.neighbours[3], self.neighbours[2], self.neighbours[1]]
        else:
            self.contents = self.contents[::-1]
            self.edges = [reversebits(self.edges[2]), reversebits(self.edges[1]), reversebits(self.edges[0]), reversebits(self.edges[3])]
            self.neighbours = [self.neighbours[2], self.neighbours[1], self.neighbours[0], self.neighbours[3]]

    def align(self, target):
        if target not in self.neighbours: print("Oops")
        targetdir = (target.neighbours.index(self) + 2) % 4
        while targetdir != self.neighbours.index(target): self.rotate()
        if self.edges[targetdir] in target.edges:
            self.flip(targetdir)
        return True

with open('input') as f:
    tilelist = []
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        tilenum = int(curline[5:9])
        tiledata = []
        while True:
            curline = f.readline().strip()
            if len(curline) == 0: break
            tiledata.append(curline)
        tilelist.append(Tile(tilenum, tiledata))

for curtile in tilelist:
    matchlist = [None, None, None, None]
    for i in range(len(curtile.edges)):
        for comptile in tilelist:
            if curtile.tilenum == comptile.tilenum: continue
            if curtile.edges[i] in comptile.edges or reversebits(curtile.edges[i]) in comptile.edges:
                matchlist[i] = comptile
                continue
    curtile.addneighbours(matchlist)

for curtile in tilelist:
    if curtile.iscorner() is not None:
        while curtile.iscorner() > 0: curtile.rotate()
        break
tilegrid = [[curtile]]

while tilegrid[-1][0].neighbours[2] is not None:
    if len(tilegrid[0]) > 1:
        newtile = tilegrid[-1][0].neighbours[2]
        newtile.align(tilegrid[-1][0])
        tilegrid.append([newtile])
    while tilegrid[-1][-1].neighbours[1] is not None:
        newtile = tilegrid[-1][-1].neighbours[1]
        newtile.align(tilegrid[-1][-1])
        tilegrid[-1].append(newtile)

stringgrid = []
tilesize = len(tilegrid[0][0].contents)
for currow in tilegrid:
    stringgrid += [""]*tilesize
    for curtile in currow:
        for i in range(tilesize):
            stringgrid[i-tilesize] += curtile.contents[i]

for i in stringgrid: print(i)
oldgrid = stringgrid.copy()
counter = 0
for row in stringgrid: counter += row.count("#")
print(counter)
for i in range(2):
    for j in range(4):
#        stringgrid = oldgrid.copy()
        for k in range(len(stringgrid)):
            for l in range(len(stringgrid[k])):
                findmonster(k, l, i, j)
        counter = 0
        for row in stringgrid: counter += row.count("#")
        print(counter)

for i in stringgrid: print(i)
