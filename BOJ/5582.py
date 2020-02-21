import sys
s1 = '0' + sys.stdin.readline()[:-1]
s2 = '0' + sys.stdin.readline()[:-1]
l = len(s1)
l2 = len(s2)
max_len = 0 

common_str = [[0]*l2 for _ in range(l)]

for i in range(1, l):
    for j in range(1, l2):
        if s1[i] == s2[j]:
            common_str[i][j] = common_str[i-1][j-1] + 1
            max_len = max(max_len, common_str[i][j])

print(max_len)