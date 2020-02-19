import sys

deque = []

def push_front(n):
    deque.insert(0, n)
def push_back(n):
    deque.append(n)
def pop_front():
    print(-1 if not deque else deque.pop(0))
def pop_back():
    print(-1 if not deque else deque.pop())
def size():
    print(len(deque))
def empty():
    print(1 if not deque else 0)
def front():
    print(-1 if not deque else deque[0])
def back():
    print(-1 if not deque else deque[-1])

command = {
    "push_front": push_front,
    "push_back": push_back,
    "pop_front": pop_front,
    "pop_back": pop_back,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back,
}

for case in range(int(sys.stdin.readline())):
    cmd_lst = sys.stdin.readline().split()
    if cmd_lst[0].startswith("push"): command[cmd_lst[0]](cmd_lst[1])
    else: command[cmd_lst[0]]()