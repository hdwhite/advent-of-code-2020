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
        if pinfo[0] == "byr": 
            if pinfo[1].isdigit() and int(pinfo[1]) > 1919 and int(pinfo[1]) < 2003: validation = validation + 1
        if pinfo[0] == "iyr":
            if pinfo[1].isdigit() and int(pinfo[1]) > 2009 and int(pinfo[1]) < 2021: validation = validation + 2
        if pinfo[0] == "eyr":
            if pinfo[1].isdigit() and int(pinfo[1]) > 2019 and int(pinfo[1]) < 2031: validation = validation + 4
        if pinfo[0] == "hgt":
            if len(pinfo[1]) == 5 and pinfo[1][3:5] == "cm":
                if pinfo[1][0:3].isdigit() and int(pinfo[1][0:3]) > 149 and int(pinfo[1][0:3]) < 194: validation = validation + 8
            elif len(pinfo[1]) == 4 and pinfo[1][2:4] == "in":
                if pinfo[1][0:2].isdigit() and int(pinfo[1][0:2]) > 58 and int(pinfo[1][0:2]) < 77: validation = validation + 8
        if pinfo[0] == "hcl":
            if re.search(r'^#[\da-f]{6}$', pinfo[1]): validation = validation + 16
        if pinfo[0] == "ecl":
            if re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', pinfo[1]): validation = validation + 32
        if pinfo[0] == "pid":
            if re.search(r'^[0-9]{9}$', pinfo[1]): validation = validation + 64
if validation == 127: numvalid = numvalid + 1

print(numvalid)
