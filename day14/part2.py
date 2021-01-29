import re
with open('input') as f:
    commandlist = f.read().splitlines()

memory = {}
for command in commandlist:
    if command[0:4] == "mask":
        curmask = command[7:]
    else:
        memdata = re.findall(r'^mem\[(\d+)\] = (\d+)$', command)
        addresslist = [int(memdata[0][0])]
        value = int(memdata[0][1])
        for i in range(len(curmask)):
            if curmask[-1 - i] == "1":
                addresslist = list(map(lambda x:x | (1 << i), addresslist))
            elif curmask[-1 - i] == "X":
                for j in range(len(addresslist)):
                    addresslist[j] |= (1 << i)
                    addresslist.append(addresslist[j] - (1 << i))
        for x in addresslist:
            print(bin(x))
        for address in addresslist: memory[address] = value
print(sum(memory.values()))
