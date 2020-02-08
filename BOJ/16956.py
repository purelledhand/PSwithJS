R, C = map(int, input().split())
M = [list(input()) for i in range(R)]
#ESWN
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
fail = False

#def dfs(wolf_x, wolf_y):

#can't solve problem check
for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4):
                ii, jj = i+dx[w], j+dy[w]
                if ii < 0 or ii >= R or jj < 0 or jj >= C:
                    continue
                if M[ii][jj]=='S': fail = True

#greedy
for i in range(R):
    for j in range(C):
        if M[i][j] not in 'SW':
            M[i][j] = 'D'

if fail: print(0)
else:
    print(1)
    for i in range(R):
        print(''.join(list(map(str,M[i]))))