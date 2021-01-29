with open('input') as f:
    timestamp = int(f.readline())
    busdata = f.readline().split(",")

curtime = 0
hasmatch = list(map(lambda x:x == "x", busdata))
multiplier = 1
while not min(hasmatch):
    curtime += multiplier
    display = []
    for i in range(len(busdata)):
        if busdata[i] == "x": display.append("-")
        else:
            remainder = (-1 * curtime) % int(busdata[i])
            display.append(remainder)
        if (not hasmatch[i]) and remainder == i % int(busdata[i]):
            hasmatch[i] = True
            multiplier *= int(busdata[i])
    print(*display, sep=' ')
print(curtime)
