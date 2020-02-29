T = int(input())

def process():
    M, N, K = map(int, input().split())
    target = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(0, K):
        x, y = map(int, input().split())
        target[x][y] = 1
    
    for i in target:
        print(' '.join(list(map(str,i))))
        

for _ in range(0, T):
    process()