N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]
seq = []
bef = 0
cur = 0
while circle:
    bef = cur
    cur = ((bef+K-1)%len(circle))
    seq.append(circle.pop(cur))
    
print("<"+str(seq)[1:-1]+">")