def getcombos(sublist):
    if len(sublist) < 3: return 1
    total = 0
    for i in range(1, len(sublist)):
        if sublist[i] - sublist[0] < 4: total += getcombos(sublist[i:])
        else: break
    return total

with open('input') as f:
    joltlist = f.read().splitlines()
joltlist = list(map(int, joltlist))

joltlist.append(0)
joltlist.sort()
joltlist.append(joltlist[-1] + 3)

threegaps = [0]
for i in range(1, len(joltlist)):
    if joltlist[i-1] + 3 == joltlist[i]: threegaps.append(i)

combinations = 1
for i in range(1, len(threegaps)):
    combinations *= getcombos(joltlist[threegaps[i-1]:threegaps[i]])
print combinations
