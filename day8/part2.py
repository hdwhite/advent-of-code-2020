with open('input') as f:
    assemblyfile = f.read().splitlines()

for i in range(len(assemblyfile)):
    if assemblyfile[i][0:3] == "acc": continue

    lines = dict()
    linenum = 0
    curvalue = 0
    while not linenum in lines:
        curline = assemblyfile[linenum]
        lines[linenum] = curvalue
        if curline[0:3] == "acc":
            curvalue += int(curline[4:])
            linenum += 1
        elif curline[0:3] == "nop":
            if i == linenum: linenum += int(curline[4:])
            else: linenum += 1
        else:
            if i == linenum: linenum += 1
            else: linenum += int(curline[4:])

        if linenum == len(assemblyfile):
            print(curvalue)
            quit()
        if linenum > len(assemblyfile):
            break
