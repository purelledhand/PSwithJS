import time
start = time.time()
for case in range(1, int(input())+1):
    S = input()
    sep_io = []
    cnt = 0
    for i in S:
        if i == 'I' or i == 'i':
            sep_io.append(i)
        elif i == 'O':
            if 'I' in sep_io:
                sep_io[sep_io.index('I')] += i
            elif 'i' in sep_io:
                sep_io[sep_io.index('i')] += i
        elif i == 'o':
            if 'i' in sep_io:
                sep_io[sep_io.index('i')] += i
            elif 'I' in sep_io:
                sep_io[sep_io.index('I')] += i
        
    
    print(sep_io)
    for i in sep_io:
        if i == 'IO':
            cnt += 1
    print("Case #{}: {}".format(case, cnt))
print("time :", time.time() - start)