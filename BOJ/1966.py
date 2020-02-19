for case in range(int(input())):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    target = q[M]
    while max(q) != q[0]:
        q.append(q[0])
        q.pop(1)
    print(nq.index(target)+1)