import sys

def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))
    return visited

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(0, M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i = i.sort()

print(graph)

print(" ".join(map(str,dfs(graph, V))))
print(" ".join(map(str,bfs(graph, V))))