def reversebits(n):
    result = 0
    for i in range(10):
        result = result << 1 | (n & 1)
        n = n >> 1
    return result

with open('input') as f:
    tilelist = {}
    edgelist = {}
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        tilenum = int(curline[5:9])
        tiledata = []
        edges = [0, 0, 0, 0]
        while True:
            curline = f.readline().strip()
            if len(curline) == 0: break
            tiledata.append(curline)
            edges[1] = (edges[1] << 1) | (curline[-1] == "#")
            edges[3] = (edges[3] << 1) | (curline[0] == "#")
        for curchar in tiledata[0]: edges[0] = (edges[0] << 1) | (curchar == "#")
        for curchar in tiledata[-1]: edges[2] = (edges[2] << 1) | (curchar == "#")
        tilelist[tilenum] = tiledata
        edgelist[tilenum] = edges

print(edgelist)

counter = 1
for tilenum, edges in edgelist.items():
    matchlist = [[], [], [], []]
    for i in range(len(edges)):
        for comptile, compedges in edgelist.items():
            if tilenum == comptile: continue
            if edges[i] in compedges or reversebits(edges[i]) in compedges:
                matchlist[i].append(comptile)
    isedge = 0
    for i in matchlist:
        if len(i) == 0:
            if isedge: counter *= tilenum
            isedge = 1
    print(tilenum, matchlist)
print(counter)
