import re
with open('input.txt') as f:
    passwordlist = f.read().splitlines()

numvalid = 0
for pline in passwordlist:
    pdata = re.findall(r'^(\d+)-(\d+) (\w):( \w+)$', pline)
    firstpos = int(pdata[0][0])
    secondpos = int(pdata[0][1])
    matchletter = pdata[0][2]
    password = pdata[0][3]
    if bool(password[firstpos] == matchletter) ^ bool(password[secondpos] == matchletter): numvalid = numvalid + 1
    print(pline, numvalid)
print(numvalid)
