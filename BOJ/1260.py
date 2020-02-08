def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))
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

N, M, V = map(int, input().split())
graph = dict()

for i in range(0, M):
    A, B = map(int, input().split())
    if A not in graph.keys():
        graph[A] = list()
    if B not in graph.keys():
        graph[B] = list()
    graph[A].append(B)
    graph[B].append(A)

print(" ".join(map(str,dfs(graph, V))))
print(" ".join(map(str,bfs(graph, V))))