import re

def has_gold(color):
    for subcolor in rules[color]:
        if subcolor == "shiny gold": return True
        if has_gold(subcolor): return True
    return False


with open('input') as f:
    baggagefile = f.read().splitlines()

rules = dict()
for line in baggagefile:
    bagparse = re.findall(r'^(.+) bags contain (.+)$', line)
    bagname = bagparse[0][0]
    contents = re.findall(r'\d ([\w\s]+) bag', bagparse[0][1])
    rules[bagname] = contents

numvalid = 0
for color in rules:
    if has_gold(color): numvalid += 1

print(numvalid)
