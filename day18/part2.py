with open('input') as f:
    expressionlist = f.read().splitlines()

total = 0
for curexp in expressionlist:
    newexp = []
    stack = []
    for token in curexp:
        if token == " ": continue
        elif token.isnumeric(): newexp.append(token)
        elif token == "+" and (len(stack) == 0 or stack[-1] == "*"): stack.append(token)
        elif token == "*" or token == "+":
            while len(stack) > 0 and (stack[-1] != "(" and (stack[-1] == "+" or token == "*")):
                newexp.append(stack.pop())
            stack.append(token)
        elif token == "(": stack.append(token)
        elif token == ")":
            while stack[-1] != "(": newexp.append(stack.pop())
            stack.pop()
        else: print("Oops", token)
    while len(stack) > 0:
        newexp.append(stack.pop())
    
    for i in newexp:
        if i.isnumeric(): stack.append(int(i))
        elif i == "+": stack.append(stack.pop() + stack.pop())
        elif i == "*": stack.append(stack.pop() * stack.pop())
        else: print("Oops", newexp)
    total += stack[0]
    if len(stack) != 1:
        print(curexp, newexp, stack)
        quit()
    print(curexp, ' '.join(newexp), stack)

print(total)
