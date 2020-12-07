with open('input.txt') as f:
    passfile = f.read().splitlines()

seatids = []
for bpass in passfile:
    curid = 0
    for row in range(10):
        if bpass[row] == 'B' or bpass[row] == 'R': curid += 2**(9-row)
    seatids.append(curid)

seatids.sort()
for curseat in seatids:
    if seatids[curseat + 1] - seatids[curseat] == 2:
        print(seatids[curseat] + 1)
        break
