lst = []
for i in range(0, 9):
    lst.append(int(input()))

max_n = max(lst)
print(max_n)
print(lst.index(max_n)+1)