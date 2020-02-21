import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
primes = [2, 3]
m = max(numbers)
cnt = 0

for i in range(4, m+1):
    for p in primes:
        if i%p == 0: break
        if p == primes[-1]: primes.append(i)

for i in numbers:
    if i in primes: cnt += 1

print(cnt)