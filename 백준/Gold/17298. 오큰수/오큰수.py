import sys
from collections import deque
from itertools import islice

def next_greater_element(seq_size, seq):
    result = [-1] * seq_size
    stack = []

    for i in range(seq_size):
        while stack and seq[stack[-1]] < seq[i]:
            idx = stack.pop()
            result[idx] = seq[i]
        stack.append(i)
    print(*result)

seq_size = int(sys.stdin.readline().strip())
seq = list(map(int, sys.stdin.readline().strip().split()))

next_greater_element(seq_size, seq)