def updatescore(deck):
    global score
    score = 0
    for i in range(len(deck)): score += (i+1) * deck[-1 - i]

def subgame(deck1, deck2):
    history = []
    print("New subgame with " + str(len(deck1)) + " and " + str(len(deck2)) + " cards.")
    print(deck1, deck2)
    numrounds = 0
    while len(deck1)*len(deck2):
        if (deck1+[0]+deck2) in history:
            updatescore(deck1)
            print("Repeat of round " + str(history.index(deck1+[0]+deck2)) + ". Player 1 wins after " + str(numrounds) + " rounds.")
            return 1
        history.append(deck1+[0]+deck2)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 <= len(deck1) and card2 <= len(deck2):
            winner = subgame(deck1[:card1], deck2[:card2])
            print(deck1, deck2)
        else:
            winner = 2 - (card1 > card2)

        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
        print(deck1, deck2)
        numrounds += 1
    updatescore(deck1 + deck2)
    print("Player " + str((len(deck1) == 0) + 1) + " wins after " + str(numrounds) + " rounds.")
    return (len(deck1) == 0) + 1

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

subgame(deck1, deck2)
print(score)
