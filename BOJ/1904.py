N = int(input())
tile = [1, 2] + [0 for _ in range(N-2)]

for i in range(2, N):
    tile[i] = (tile[i-1] + tile[i-2])%15746
print(tile[-1])