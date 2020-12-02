with open('input.txt') as f:
    expenses = f.read().splitlines()
expenses = list(map(int, expenses))
expenses.sort()

first = 0
second = 1
third = 2
while True:
    total = expenses[first] + expenses[second] + expenses[third]
    print (first, second, third, total)
    if total == 2020:
        break
    elif total > 2020:
        if second + 1 == third:
            first = first + 1
            second = first + 1
        else:
            second = second + 1
        third = second + 1
    else:
        if third == len(expenses) - 1:
            if third - second == 1:
                first = first + 1
                second = first + 1
            else:
                second = second + 1
            third = second + 1
        else:
            third = third + 1

print(expenses[first], expenses[second], expenses[third], total, expenses[first]*expenses[second]*expenses[third])
