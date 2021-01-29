with open('input') as f:
    assemblyfile = f.read().splitlines()

lines = dict()
linenum = 0
curvalue = 0
while not linenum in lines:
    curline = assemblyfile[linenum]
    print(linenum, curline, curvalue)
    lines[linenum] = curvalue
    if curline[0:3] == "nop":
        linenum += 1
    elif curline[0:3] == "acc":
        curvalue += int(curline[4:])
        linenum += 1
    else:
        linenum += int(curline[4:])

print(curvalue)
