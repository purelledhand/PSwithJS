from itertools import product

def match(s, rule):
    if len(s) != len(rule):
        return False
    for i in range(len(rule)):
        if rule[i] != '*' and s[i] != rule[i]:
            return False
    return True

def solution(user_id, banned_id):
    match_case = [[] for _ in range(len(banned_id))]
    answer = set()

    for i in range(len(banned_id)):
        for j in user_id:
            if match(j, banned_id[i]):
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
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.07ms, 10.9MB)
테스트 3 〉	통과 (0.08ms, 10.7MB)
테스트 4 〉	통과 (0.06ms, 10.8MB)
테스트 5 〉	통과 (9683.62ms, 1.91GB)
테스트 6 〉	통과 (2.38ms, 10.8MB)
테스트 7 〉	통과 (0.06ms, 10.8MB)
테스트 8 〉	통과 (0.08ms, 10.8MB)
테스트 9 〉	통과 (0.08ms, 10.8MB)
테스트 10 〉통과 (0.06ms, 10.8MB)
테스트 11 〉통과 (0.09ms, 10.8MB)
'''