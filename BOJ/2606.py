import sys

def dfs(graph):
    visited = []
    stack = [1]
    while stack:
        if stack[-1] not in visited:
            node = stack.pop()
            visited.append(node)
            stack.extend(graph[node])
        else:
            stack.pop()
    return len(visited)-1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(dfs(graph))