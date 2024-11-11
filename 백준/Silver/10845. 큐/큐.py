import sys


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, x):
        node = Node(x)
        if not self.front:
            self.front = self.rear = Node(x)
        else:
            self.rear.next = node
            self.rear = node

    def pop(self):
        if not self.front:
            return -1
        node = self.front
        self.front = node.next
        if not self.front:
            self.rear = None
        return node.val

    def size(self):
        if not self.front:
            return 0
        node = self.front
        length = 0
        while node:
            node = node.next
            length += 1
        return length

    def empty(self):
        return 1 if not self.front else 0

    def first(self):
        return self.front.val if self.front else -1

    def back(self):
        return self.rear.val if self.rear else -1


cmd_num = int(sys.stdin.readline().strip())
input_cmd = [sys.stdin.readline().strip() for _ in range(cmd_num)]

queue = Queue()

for cmd in input_cmd:
    if cmd.startswith("push"):
        _, val = cmd.split()
        queue.push(int(val))
    elif cmd == "pop":
        print(queue.pop())
    elif cmd == "size":
        print(queue.size())
    elif cmd == "empty":
        print(queue.empty())
    elif cmd == "front":
        print(queue.first())
    else:
        print(queue.back())
