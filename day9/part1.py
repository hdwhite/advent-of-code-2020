with open('input') as f:
    fullnums = f.read().splitlines()
fullnums = list(map(int, fullnums))

previous = []
for i in range(len(fullnums)):
    if len(previous) < 25:
        previous.append(fullnums[i])
        continue
    target = fullnums[i]
    hasmatch = 0
    for j in previous:
        if (target - j) in previous and j*2 != target:
            previous.pop(0)
            previous.append(target)
            hasmatch = 1
            break
    if hasmatch == 0:
        print(target)
        quit()
