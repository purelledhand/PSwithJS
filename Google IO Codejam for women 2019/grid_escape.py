T = int(input())
for case in range(1, T+1):
    R, C, K = map(int, input().split())
    
    if K == R * C - 1:
        print("Case #{}: IMPOSSIBLE".format(case))
        continue
    print("Case #{}: POSSIBLE".format(case))

    escape_room = list(list('S' for _ in range(C)) for _ in range(R-1))

    if C==1:
        escape_room.append(['N'])
    else:
        escape_room.append(list('E' for _ in range(C-1)) + ['W'])

    for x in range(K):
        i, j = divmod(x, C)
        escape_room[i][j] = 'W'

    for row in escape_room:
        print(''.join(row))