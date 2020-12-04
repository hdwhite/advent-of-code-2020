import re
with open('input.txt') as f:
    passportfile = f.read().splitlines()

validation = 0
numvalid = 0
for pline in passportfile:
    if len(pline) == 0:
        if validation == 127: numvalid = numvalid + 1
        validation = 0
        continue
    pdata = re.findall(r'(\w+):(\S+)', pline)
    for pinfo in pdata:
        if pinfo[0] == "byr": validation = validation + 1
        if pinfo[0] == "iyr": validation = validation + 2
        if pinfo[0] == "eyr": validation = validation + 4
        if pinfo[0] == "hgt": validation = validation + 8
        if pinfo[0] == "hcl": validation = validation + 16
        if pinfo[0] == "ecl": validation = validation + 32
        if pinfo[0] == "pid": validation = validation + 64
if validation == 127: numvalid = numvalid + 1

print(numvalid)
