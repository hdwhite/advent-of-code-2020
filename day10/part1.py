with open('input') as f:
    joltlist = f.read().splitlines()
joltlist = list(map(int, joltlist))

joltlist.append(0)
joltlist.sort()
num1 = 0
num3 = 0
for i in range(1, len(joltlist)):
    if joltlist[i-1] + 1 == joltlist[i]: num1 += 1
    if joltlist[i-1] + 3 == joltlist[i]: num3 += 1
print(num1 * (num3+1))
