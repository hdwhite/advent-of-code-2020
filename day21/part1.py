with open('input') as f:
    inputdata = f.read().splitlines()

ingredients = dict()
inglist = set()
for curline in inputdata:
    linedata = curline[:-1].split(" (contains ")
    curing = linedata[0].split()
    inglist.update(curing) 
    allergiens = linedata[1].split(", ")
    for curall in allergiens:
        if curall not in ingredients:
            ingredients[curall] = []
        ingredients[curall].append(curing)

counter = 0
for curing in inglist:
    ingcounter = set()
    canmatch = False
    for allname, curall in ingredients.items():
        inall = True
        for curitem in curall:
            if curing in curitem: ingcounter.add(''.join(curitem))
            else: inall = False
        canmatch |= inall
    if not canmatch: counter += len(ingcounter)

print(counter)
