import sys

queue = []

def push(n):
    queue.append(n)
def pop():
    print(-1 if not queue else queue.pop(0))
def size():
    print(len(queue))
def empty():
    print(1 if not queue else 0)
def front():
    print(-1 if not queue else queue[0])
def back():
    print(-1 if not queue else queue[-1])

command = {
    "push": push,
    "pop": pop,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back,
}

for case in range(int(sys.stdin.readline())):
    cmd_lst = sys.stdin.readline().split()
    if cmd_lst[0] == "push": push(cmd_lst[1])
    else: command[cmd_lst[0]]()