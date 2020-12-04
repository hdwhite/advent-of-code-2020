with open('input.txt') as f:
    treemap = f.read().splitlines()

fieldlength = len(treemap[0])
moveright = [1, 3, 5, 7, 1]
movedown = [1, 1, 1, 1, 2]
numtrees = [0, 0, 0, 0, 0]
product = 1

for i in range(len(numtrees)):
    curpos = 0
    for index, line in enumerate(treemap):
        if index % movedown[i] == 0:
            if line[curpos] == "#": numtrees[i] = numtrees[i] + 1
            curpos = (curpos + moveright[i]) % fieldlength
    product = product * numtrees[i]

print(numtrees, product)
