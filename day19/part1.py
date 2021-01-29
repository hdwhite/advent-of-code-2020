def getstr(test, rule):
    validstrings = set()
    for option in rules[rule]:
        if not option[0].isnumeric():
            if option[0][1] == test[0]:
                return set([test[0]])
            else:
                return set()
        if len(option) == 1:
            validstrings |= getstr(test, int(option[0]))
        else:
            stringoptions = getstr(test, int(option[0]))
            for firststr in stringoptions:
                if len(firststr) >= len(test): continue
                validstrings |= set(map(lambda x:firststr + x, getstr(test[len(firststr):], int(option[1]))))
#        print(test, option, validstrings)
    return validstrings

def isvalid(test, rule):
    for curstr in getstr(test, rule):
        if test == curstr: return True
    return False


with open('input') as f:
    rules = {}
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        key = int(curline[:curline.index(":")])
        curline = curline[curline.index(" ")+1:]
        values = curline.split(" | ")
        values = list(map(lambda x:tuple(x.split(" ")), values))
        rules[key] = values

    testlist = []
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        testlist.append(curline)

counter = 0
for teststr in testlist:
    counter += isvalid(teststr, 0)
print(counter)
