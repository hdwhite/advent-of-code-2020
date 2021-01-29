with open('input') as f:
    f.readline()
    deck1 = []
    deck2 = []
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        deck1.append(int(curline))
    f.readline()
    while True:
        curline = f.readline().strip()
        if len(curline) == 0: break
        deck2.append(int(curline))

while len(deck1)*len(deck2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)
    print(deck1, deck2)

score = 0
finaldeck = deck1[::-1] + deck2[::-1]
for i in range(len(finaldeck)): score += (i+1) * finaldeck[i]
print(score)
