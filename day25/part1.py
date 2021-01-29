with open('input') as f:
    key1 = int(f.readline().strip())
    key2 = int(f.readline().strip())


print(key1, key2)

loop1 = 0
loop2 = 0
key = 1
steps = 0
while not loop1*loop2:
    key = (7*key) % 20201227
    steps += 1
    if key == key1: loop1 = steps
    if key == key2: loop2 = steps

subject = key
key = 1
for i in range(min(loop1, loop2)):
    key = (subject * key) % 20201227
print(loop1, loop2, key)
