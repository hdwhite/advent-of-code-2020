def get_invalid(fullnums):
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
            return target

with open('input') as f:
    fullnums = f.read().splitlines()
fullnums = list(map(int, fullnums))

target = get_invalid(fullnums)
for i in range(len(fullnums)):
    cursum = 0
    for j in range(i, len(fullnums)):
        cursum += fullnums[j]
        if cursum == target:
            print(min(fullnums[i:j+1]) + max(fullnums[i:j+1]))
            quit()
        elif cursum > target:
            break
