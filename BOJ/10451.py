import sys

def dfs(start, graph, visited):
    stack = [start]
    while stack:
        if visited[stack[-1]] is False:
            node = stack.pop()
            visited[node] = True
            stack.extend(graph[node])
        else:
            stack.pop()
        
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    seq = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False]*(N+1)
    cc = 0
    for i in range(1, N+1):
        u = seq[i]
        v = seq[u]
        if v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
    
    for i in range(1, N+1):
        if visited[i] is False:
            dfs(i, graph, visited)
            cc += 1
    print(cc)