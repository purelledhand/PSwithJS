import sys
lst = []
stack = []
index = 0
stack_num = 1
result = []
result_op = []
N = int(sys.stdin.readline())
for seq in range(N):
    lst.append(int(sys.stdin.readline()))

while len(result)<N:
    if lst[index] >= stack_num:
        stack.append(stack_num)
        result_op.append('+')
        stack_num += 1
    else:
        s = stack.pop()
        if s != lst[index]:
            print('NO')
            exit()
        result.append(s)
        result_op.append('-')
        index += 1

print('\n'.join(result_op))