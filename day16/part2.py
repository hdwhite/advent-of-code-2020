import re

with open('input') as f:
    category = {}
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        linedata = re.findall(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', curline)
        category[linedata[0][0]] = (int(linedata[0][1]), int(linedata[0][2]), int(linedata[0][3]), int(linedata[0][4]))

    f.readline()
    curline = f.readline()
    yourticket = list(map(int, curline.split(",")))
    f.readline()
    f.readline()
   
    nearby = []
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        nearby.append(list(map(int, curline.split(","))))

valid = [yourticket]
for curticket in nearby:
    ismismatch = 0
    for curitem in curticket:
        hascategory = 0
        for curcat, catnums in category.items():
            if (curitem >= catnums[0] and curitem <= catnums[1]) or (curitem >= catnums[2] and curitem <= catnums[3]):
                hascategory = 1
                break
        if hascategory == 0:
            ismismatch = 1
            break
    if ismismatch: continue
    valid.append(curticket)

hasmatches = {}
for curcat, catnums in category.items():
    possible = [1]*len(valid[0])
    for curticket in valid:
        for i in range(len(curticket)):
            if curticket[i] < catnums[0] or (curticket[i] > catnums[1] and curticket[i] < catnums[2]) or curticket[i] > catnums[3]:
                possible[i] = 0
    hasmatches[curcat] = possible

maxmatches = 999
while maxmatches > 1:
    maxmatches = 0
    newmatch = hasmatches.copy()
    for curcat, catmatches in hasmatches.items():
        nummatches = sum(catmatches)
        maxmatches = max(maxmatches, nummatches)
        if nummatches == 0:
            print(hasmatches)
            print("Error")
            quit()
        if nummatches == 1:
            clear = catmatches.index(1)
            for tempcat in hasmatches.keys():
                if tempcat != curcat: newmatch[tempcat][clear] = 0
    hasmatches = newmatch
    print(hasmatches)

counter = 1
for curcat, catmatches in hasmatches.items():
    if curcat[0:6] != "depart": continue
    counter *= yourticket[catmatches.index(1)]
print(counter)
