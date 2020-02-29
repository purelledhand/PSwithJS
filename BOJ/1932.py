# A[i][j] : i,j에 도착했을 때 합의 최댓값
N = int(input())
A = [[0 for _ in range(N+1)] for _ in range(N+1)]
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    tmp = [0] + list(map(int,input().split()))
    for j in range(1, i+1):
        A[i][j] = tmp[j]
DP[1][1] = A[1][1]
for i in range(2, N+1):
    for j in range(0, i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]

print(max(DP[N]))