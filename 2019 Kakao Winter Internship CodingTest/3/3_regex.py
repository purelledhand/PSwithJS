# regex 사용시 시간초과

import re
from itertools import product

def solution(user_id, banned_id):
    reg = [[] for _ in range(len(banned_id))]
    match_case = [[] for _ in range(len(banned_id))]
    answer = set()

    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace('*','.')
        reg[i] = re.compile(banned_id[i])

    for i in range(len(reg)):
        for j in user_id:
            if reg[i].match(j) and len(banned_id[i]) == len(j):
                match_case[i].append(j)
                
    banned = list(product(*match_case))

    for r in banned:
        if len(set(r)) == len(banned_id):
            answer.add(", ".join(sorted(set(r))))

    return len(answer)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])

'''
테스트 1 〉	통과 (0.08ms, 10.8MB)
테스트 2 〉	통과 (0.20ms, 10.8MB)
테스트 3 〉	통과 (0.16ms, 10.7MB)
테스트 4 〉	통과 (0.18ms, 10.8MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (2.39ms, 10.8MB)
테스트 7 〉	통과 (0.18ms, 10.6MB)
테스트 8 〉	통과 (0.21ms, 10.8MB)
테스트 9 〉	통과 (0.20ms, 10.8MB)
테스트 10 〉통과 (0.29ms, 10.8MB)
테스트 11 〉통과 (0.25ms, 10.8MB)
'''