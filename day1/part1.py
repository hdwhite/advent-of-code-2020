with open('input.txt') as f:
    expenses = f.read().splitlines()
expenses = list(map(int, expenses))
expenses.sort()

left = 1
right = -1
while expenses[left] + expenses[right] != 2020:
    print(left, "\t", expenses[left], "\t", right, "\t", expenses[right])
    if expenses[left] + expenses[right] > 2020: right = right-1
    if expenses[left] + expenses[right] < 2020: left = left+1

print("Small: ", expenses[left], "\tLarge: ", expenses[right], "\tTotal", (expenses[left]*expenses[right]))
