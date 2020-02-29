N, K = map(int, input().split())

def bfs():
    graph = [0]*100001
    que = [N]
    while que:
        cur = que.pop(0)
        if cur == K:
            return graph[cur]
        for next in [cur-1, cur+1, 2*cur]:
            if 0<=next<100001 and graph[next]==0:
                que.append(next)
                graph[next] = graph[cur]+1
    
print(bfs())