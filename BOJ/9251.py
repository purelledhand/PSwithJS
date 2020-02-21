import sys
s1 = sys.stdin.readline()[:-1]
s2 = sys.stdin.readline()[:-1]
l = len(s1)+1
l2 = len(s2)+1

lcs = [[0]*l2 for _ in range(l)]

for i in range(1, l):
    for j in range(1, l2):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[l-1][l2-1])