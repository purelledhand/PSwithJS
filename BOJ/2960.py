N, K = map(int, input().split())
arr = [False, False, True] + [True for _ in range(0,N-2)]
erased = []
for i in range(2, N+1):
    if arr[i]:
        for p in range(i, N+1, i):
            if arr[p]:
                arr[p] = False
                erased.append(p)
print(erased[K-1])