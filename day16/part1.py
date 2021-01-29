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
    yourticket = curline.split(",")
    f.readline()
    f.readline()
   
    nearby = []
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        nearby.append(list(map(int, curline.split(","))))

counter = 0
for curticket in nearby:
    ismismatch = 0
    for curitem in curticket:
        hascategory = 0
        for curcat, catnums in category.items():
            if (curitem > catnums[0] and curitem < catnums[1]) or (curitem > catnums[2] and curitem < catnums[3]):
                hascategory = 1
                break
        if hascategory == 0:
            counter += curitem
            ismismatch = 1
            break
    if ismismatch: continue

print(counter)
