import sys
from collections import deque

def stack_seq(target_seq, n):
    stack = []
    ops = []
    current = 1
    target_seq = deque(target_seq)

    while current <= n:
        stack.append(current)
        ops.append('+')
        current += 1
        
        while stack and stack[-1] == target_seq[0]:
            stack.pop()
            target_seq.popleft()
            ops.append('-')

    while stack:
        if not target_seq or stack[-1] != target_seq[0]:
            print('NO')
            return
        stack.pop()
        target_seq.popleft()
        ops.append('-')

    return print('\n'.join(ops))

input = list(map(int, sys.stdin.read().splitlines()))

stack_seq(input[1:], input[0])