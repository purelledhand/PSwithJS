import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
sums = []
for i in numbers:
    for j in numbers:
        if i == j: continue
        for k in numbers:
            if j == k or i == k: continue
            if (i+j+k)<=M: sums.append(i+j+k)

print(max(sums))