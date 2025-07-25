import sys
from collections import deque

def push_front(x):
    return deq.appendleft(x)

def push_back(x):
    return deq.append(x)

def pop_front():
    return print(deq.popleft() if deq else -1)

def pop_back():
    return print(deq.pop() if deq else -1)

def size():
    return print(len(deq))

def empty():
    return print(0 if deq else 1)

def front():
    return print(deq[0] if deq else -1)

def back():
    return print(deq[-1] if deq else -1)

cmd_map = {
    'push_front': lambda x: push_front(x),
    'push_back': lambda x: push_back(x),
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

def process_deque(cmd_list):
    for cmd in cmd_list:
        if cmd.startswith('push_front'):
            cmd, x = cmd.split()
            cmd_map[cmd](x)
        elif cmd.startswith('push_back'):
            cmd, x = cmd.split()
            cmd_map[cmd](x)
        else:
            cmd_map[cmd]()

deq = deque([])
cmd_num = int(sys.stdin.readline().strip())
cmd_list = sys.stdin.read().splitlines()

process_deque(cmd_list)