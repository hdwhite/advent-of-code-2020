with open('input.txt') as f:
    treemap = f.read().splitlines()

fieldlength = len(treemap[0])
curpos = 0
numtrees = 0
for line in treemap:
    if line[curpos] == "#": numtrees = numtrees + 1
    curpos = (curpos + 3) % fieldlength

print(numtrees)
