def calculate(s):
    def update(op, v):
        if op == '+': stack.append(v)
        if op == '-': stack.append(-v)

    i, num, stack, sign = 0, 0, [], '+'
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] in '+-':
            update(sign, num)
            num, sign = 0, s[i]
        elif s[i] == '(':
            j = i
            bal = 0
            while i < len(s):
                if s[i] == '(': bal += 1
                if s[i] == ')': bal -= 1
                if bal == 0: break
                i += 1
            num = calculate(s[j + 1:i])
        i += 1
    update(sign, num)
    return sum(stack)


print(calculate("1 + 1"))
print(calculate("2-1 + 2"))  
