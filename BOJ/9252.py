import sys

s1 = sys.stdin.readline()[:-1]
s2 = sys.stdin.readline()[:-1]
l = len(s1)
l2 = len(s2)
result = ''
lcs = [[0]*(l2+1) for _ in range(l+1)]

for i in range(1, l+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else: lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

a, b = l, l2
while lcs[a][b] != 0:
    if lcs[a][b] == lcs[a-1][b]:
        a -= 1
    elif lcs[a][b] == lcs[a][b-1]:
        b -= 1
    elif lcs[a][b]-1 == lcs[a-1][b-1]:
        result += s1[a-1]
        a-=1
        b-=1

print(lcs[l][l2])
print(result[::-1])