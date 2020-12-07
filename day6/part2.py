with open('input.txt') as f:
    questionfile = f.read().splitlines()

total = 0
answerlist = [1]*26
for line in questionfile:
    if len(line) == 0:
        total += sum(answerlist)
        answerlist = [1]*26
        continue
    curanswers = [0]*26
    for answer in line:
        curanswers[ord(answer)-97] = 1
    for i in range(len(answerlist)):
        answerlist[i] = answerlist[i] & curanswers[i]

total += sum(answerlist)
print(total)
