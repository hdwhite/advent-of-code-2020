import re
with open('input') as f:
    commandlist = f.read().splitlines()

memory = {}
for command in commandlist:
    if command[0:4] == "mask":
        curmask = command[7:]
    else:
        memdata = re.findall(r'^mem\[(\d+)\] = (\d+)$', command)
        address = memdata[0][0]
        value = int(memdata[0][1])
        for i in range(len(curmask)):
            if curmask[-1 - i] == "1":
                value |= (1 << i)
            elif curmask[-1 - i] == "0":
                value &= (1 << len(curmask)) - 1 - (1 << i)
        print(value)
        memory[address] = value
print(sum(memory.values()))
