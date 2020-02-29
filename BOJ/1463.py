N = int(input())
d = [0, 0, 1, 1] + [0 for _ in range(N-3)]

for i in range(4, N+1):
    d[i] = d[i-1]+1
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    elif i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[N])