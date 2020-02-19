import sys
S = []
for case in range(int(sys.stdin.readline())):
    S.append(sys.stdin.readline()[:-1])
S=list(set(S))
S.sort()
S.sort(key=len)
print('\n'.join(S))