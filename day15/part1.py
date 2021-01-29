numlist = [11,18,0,20,1,7,16]
numlist.reverse()

while len(numlist) < 2020:
    if numlist[0] not in numlist[1:]:
        numlist.insert(0, 0)
    else:
        numlist.insert(0, (numlist[1:]).index(numlist[0]) + 1)

print(numlist[0])
