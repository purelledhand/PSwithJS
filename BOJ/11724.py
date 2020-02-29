import sys

def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = []
cc = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        cc += 1

print(cc)



