import sys


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return -1
        node = self.top
        self.top = node.next
        return node.val

    def size(self):
        node = self.top
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def empty(self):
        return 1 if not self.top else 0

    def peek(self):
        if not self.top:
            return -1
        return self.top.val


cmd_num = int(sys.stdin.readline().strip())
cmd_lst = [sys.stdin.readline().strip() for _ in range(cmd_num)]

stack = Stack()

for cmd in cmd_lst:
    if cmd.startswith("push"):
        _, val = cmd.split()
        stack.push(int(val))
    elif cmd == "pop":
        print(stack.pop())
    elif cmd == "size":
        print(stack.size())
    elif cmd == "empty":
        print(stack.empty())
    else:
        print(stack.peek())
