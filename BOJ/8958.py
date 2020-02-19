for case in range(int(input())):
    S = input()
    sum = 0
    cnt = 0
    for i in S:
        if i == 'O': cnt += 1
        else: cnt = 0
        sum += cnt
    print(sum)