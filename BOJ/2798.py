import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

result = 0
l = len(numbers)

for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            if (numbers[i]+numbers[j]+numbers[k]) == M:
                print(M)
                exit()
            elif (numbers[i]+numbers[j]+numbers[k]) < M:
                result = max(result, numbers[i]+numbers[j]+numbers[k])

print(result)