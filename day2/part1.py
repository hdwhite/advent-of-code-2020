import re
with open('input.txt') as f:
    passwordlist = f.read().splitlines()

numvalid = 0
for pline in passwordlist:
    pdata = re.findall(r'^(\d+)-(\d+) (\w): (\w+)$', pline)
    minletter = int(pdata[0][0])
    maxletter = int(pdata[0][1])
    matchletter = pdata[0][2]
    password = pdata[0][3]
    nummatches = password.count(matchletter)
    if nummatches >= minletter and nummatches <= maxletter: numvalid = numvalid + 1
    print(pline, nummatches, numvalid)
print(numvalid)
