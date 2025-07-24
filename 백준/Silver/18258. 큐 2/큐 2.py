import sys
from collections import deque

queue = deque([])

def push(x):
    queue.append(x)

def pop():
    print(queue.popleft() if queue else -1)

def size():
    print(len(queue))

def empty():
    print(0 if queue else 1)

def front():
    print(queue[0] if queue else -1)

def back():
    print(queue[-1] if queue else -1)


cmd_map = {
    'push': lambda x: push(x),
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back,
}

cmd_num = int(sys.stdin.readline().strip())
cmd_list = sys.stdin.read().splitlines()

for cmd in cmd_list:
    if cmd.startswith('push'):
       cmd, x = cmd.split()
       cmd_map[cmd](x)
    else:
        cmd_map[cmd]()