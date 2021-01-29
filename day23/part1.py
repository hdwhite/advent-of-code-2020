def mod9(i):
    if i == 1: return 9
    else: return i-1

cups = [5, 3, 8, 9, 1, 4, 7, 6, 2]
for i in range(100):
    print(cups)
    destination = mod9(cups[0])
    while destination in cups[1:4]: destination = mod9(destination)
    for j in range(3):
        num = cups.pop(1)
        cups.insert(cups.index(destination) + j + 1, num)
    cups.append(cups.pop(0))
print(cups)
