with open('input') as f:
    timestamp = int(f.readline())
    buslist = f.readline().split(",")

bestbus = (999, 999)
for curbus in buslist:
    if curbus == "x": continue
    wait = (-1 * timestamp) % int(curbus)
    if wait < bestbus[1]: bestbus = (curbus, wait)

print(bestbus, int(bestbus[0]) * bestbus[1])
