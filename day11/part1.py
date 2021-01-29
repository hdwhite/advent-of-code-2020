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
            occupiednear = sum(list(map(lambda x:x[max(0, j-1):min(j+2, len(x))].count("#"), seatlist))[max(0, i-1):min(i+2, len(seatlist))]) - (seatlist[i][j] == "#")
            if seatlist[i][j] == ".": newseatlist[i].append(".")
            elif seatlist[i][j] == "L":
                if occupiednear == 0: newseatlist[i].append("#")
                else: newseatlist[i].append("L")
            else:
                if occupiednear < 4: newseatlist[i].append("#")
                else: newseatlist[i].append("L")
    print('\n'.join(list(map(lambda x:''.join(x), newseatlist))))
    print("")
print(sum(list(map(lambda x:x.count("#"), seatlist))))
