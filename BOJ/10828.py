import sys

stack = []

def push(n):
    stack.append(n)
def pop():
    print(-1 if not stack else stack.pop())
def size():
    print(len(stack))
def empty():
    print(1 if not stack else 0)
def top():
    print(-1 if not stack else stack[-1])

command = {
    "push": push,
    "pop": pop,
    "size": size,
    "empty": empty,
    "top": top
}

for case in range(int(sys.stdin.readline())):
    cmd_lst = sys.stdin.readline().split()
    if cmd_lst[0] == "push": push(cmd_lst[1])
    else: command[cmd_lst[0]]()