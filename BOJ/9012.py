stack = []
for case in range(int(input())):
    branket = input()
    stack = []
    for i in branket:
        if i == '(': stack.append(i)
        else:
            if(len(stack)==0):
                stack.append(i)
                break
            stack.pop()
    if len(stack) == 0: print('YES')
    else: print('NO')