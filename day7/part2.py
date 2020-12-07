import re

def num_children(color):
    total = 0
    for subcolor in rules[color]:
        total += (int(subcolor[0]) * (num_children(subcolor[1]) + 1))
    return total

with open('input') as f:
    baggagefile = f.read().splitlines()

rules = dict()
for line in baggagefile:
    bagparse = re.findall(r'^(.+) bags contain (.+)$', line)
    bagname = bagparse[0][0]
    contents = re.findall(r'(\d+) ([\w\s]+) bag', bagparse[0][1])
    rules[bagname] = contents

print(num_children("shiny gold"))
