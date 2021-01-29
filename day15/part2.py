numlist = [11,18,0,20,1,7,16]
lastseen = {}
for i in range(len(numlist) - 1):
    lastseen[numlist[i]] = i
latest = 16
print(lastseen)

for curpos in range(len(numlist) - 1, 30000000 - 1):
    if latest in lastseen:
        temp = curpos - lastseen[latest]
        lastseen[latest] = curpos
        latest = temp
    else:
        lastseen[latest] = curpos
        latest = 0
    if curpos % 100000 == 0: print(curpos)

print(latest)
