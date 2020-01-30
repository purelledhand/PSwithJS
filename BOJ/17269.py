def alpha(c):
    alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    return alpha[ord(c)-65]

def gh_operator(list):
    if(len(list)<=2): return list
    result_list = [0 for i in range(0,(len(list)-1))]
    for i in range (0, len(result_list)):
        result_list[i] = (list[i]+list[i+1])%10
    #print(result_list)
    return gh_operator(result_list)

N, M = map(int, input().split())
A, B = input().split()
result = []

gh = ''

for i in range(0, min([N,M])):
    gh += A[i]+B[i]

if(N>M): gh += A[i+1:]
elif(M>N): gh += B[i+1:]

result = list(map(alpha, gh))

#print(gh, result)

print(str(int("".join(list(map(str,gh_operator(result))))))+"%")