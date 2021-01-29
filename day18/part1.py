def evaluate(expression):
    subtotal = 0
    depth = 0
    operator = None
    value = None
    for pos, token in enumerate(expression):
        if depth < 0: return subtotal
        if token == " ": continue
        elif token == "(":
            depth += 1
            if depth == 1: value = evaluate(expression[pos+1:])
        elif token == ")": depth -= 1
        
        if depth > 0: continue
        if token == "*" or token == "+": operator = token
        elif token.isnumeric(): value = int(token)

        if value is not None:
            if operator is None: subtotal = value
            elif operator == "+": subtotal += value
            elif operator == "*": subtotal *= value
        print(expression[0:pos+1], operator, value, subtotal)
        value = None
    return subtotal

with open('input') as f:
    expressionlist = f.read().splitlines()

total = 0
for curexp in expressionlist:
    result = evaluate(curexp)
    print(curexp, result)
    total += result

print(total)
