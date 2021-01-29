with open('input') as f:
    inputdata = f.read().splitlines()

ingredients = dict()
allergymatches = dict()
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

for i in ingredients.keys(): allergymatches[i] = []

counter = 0
for curing in inglist:
    ingcounter = set()
    canmatch = False
    for allname, curall in ingredients.items():
        inall = True
        for curitem in curall:
            if curing in curitem: ingcounter.add(''.join(curitem))
            else: inall = False
        if inall: allergymatches[allname].append(curing)
        canmatch |= inall
    if not canmatch: counter += len(ingcounter)

hasupdated = True
while hasupdated:
    hasupdated = False
    newmatch = allergymatches.copy()
    for curall, curing in allergymatches.items():
        if len(curing) == 1:
            for compall, comping in allergymatches.items():
                if curall != compall and curing[0] in comping:
                    newmatch[compall].remove(curing[0])
                    hasupdated = True
    allergymatches = newmatch
    print(allergymatches)

keys = list(allergymatches.keys())
keys.sort()
result = []
for i in keys: result.append(allergymatches[i][0])
print(','.join(result))
