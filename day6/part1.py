with open('input.txt') as f:
    questionfile = f.read().splitlines()

total = 0
answerlist = [0]*26
for line in questionfile:
    if len(line) == 0:
        total += sum(answerlist)
        answerlist = [0]*26
        continue
    for answer in line:
        answerlist[ord(answer)-97] = 1

total += sum(answerlist)
print(total)
