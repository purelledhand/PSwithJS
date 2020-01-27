cnt = range(int(input()));
sum = [];
for i in cnt:
    a, b = input().split();
    sum.append(int(a)+int(b));

for i in cnt:
    print(sum[i]);