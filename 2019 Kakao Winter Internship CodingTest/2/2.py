def solution(s):
    s = s[1:-1].split('},')
    tuple_set = [ [] for _ in range(len(s))]
    answer = []
    for i in range(len(s)):
        s[i] = s[i][1:]
        if s[i][-1] == '}':
            s[i] = s[i][:-1]
        tuple_set[i] = list(map(int, s[i].split(',')))

    tuple_set.sort(key=len)
    
    print(tuple_set)

    for i in tuple_set:
        for j in i:
            if answer.count(j) == 0:
                answer.append(j)
    print(answer)
solution('{{1,2,3},{2,1},{1,2,4,3},{2}}')
