import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

primes = []
sum = 0
min_p = 10001

for i in range(2, M+1):
    if i == 2 or i == 3:
        primes.append(i)
        if i>=N:
                sum += i
                min_p = min(min_p, i)
    for p in primes:
        if i%p == 0: break
        if p == primes[-1]:
            primes.append(i)
            if i>=N:
                sum += i
                min_p = min(min_p, i)
if sum==0:
    print(-1)
    exit()

print(sum)
print(min_p)