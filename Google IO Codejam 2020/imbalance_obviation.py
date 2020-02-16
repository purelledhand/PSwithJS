for case in range(1, int(input())+1):
    N = int(input())
    down_order = list(map(int, input().split()))
    balance = 0
    r_cnt = 0
    l_cnt = 0
    index = 0
    case_order = ['LR', 'LR']

    while len(case_order[0]) < N:
        index = 0
        old_len = len(case_order)
        for i in case_order:
            balance = 0
            for a in i:
                if a == 'L': balance += 1
                else: balance -= 1

            if balance-1 >= -1:
                if index>=old_len:
                    case_order.append(i+'R')
                else:
                    case_order[index] = i+'R'
                balance -= 1
                index += 1
            if index == old_len: break;

            if balance+1 <= 1:
                if index>=old_len:
                    case_order.append(i+'L')
                else:
                    case_order[index] = i+'L'
                balance += 1
                index += 1
            if index == old_len: break;
    
    for i in case_order:
        r_cnt = i.count('R')
        l_cnt = N-r_cnt

        for o in down_order:
            if i[o-1] == 'R': r_cnt -= 1
            else: l_cnt -= 1
            if r_cnt-l_cnt > 1 or r_cnt-l_cnt < -1: break
        if r_cnt-l_cnt >= -1 and r_cnt-l_cnt <= 1:
            print("Case #{}: {}".format(case, i))
            break