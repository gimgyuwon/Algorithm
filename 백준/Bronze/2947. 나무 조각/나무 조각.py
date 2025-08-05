import sys
from collections import deque

lst = list(map(int, sys.stdin.readline().strip().split()))
idx = 0

while lst != [1,2,3,4,5]:
    if lst[idx] > lst[idx+1]:
        lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
        print(*lst)
    idx = idx + 1 if idx < 3 else 0

