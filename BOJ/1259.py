import sys
while True:
    stack = []
    S = sys.stdin.readline()[:-1]
    if S == '0': exit()
    l = len(S)
    for i in range(l):
        if i < l//2:
            stack.append(S[i])
        if i == l//2 and l%2 != 0: continue
        if i >= l//2:
            if S[i] == stack[-1]: stack.pop()
    if not stack: print('yes')
    else: print('no')