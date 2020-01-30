n, lst = int(input()), list(map(int, input().split()))
lst2 = [0 for i in range(0, len(lst))]
lst2[0] = lst[0]

for i in range(1, n):
    lst2[i] = (lst[i]*(i+1)-sum(lst2))

print(" ".join(map(str, lst2)))