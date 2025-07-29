import sys
from collections import deque

def printer_que(n, m, weight):
    count = 0
    while weight:
        biggest = max(weight, key=lambda x: x[1])[1]
        now = weight.popleft()
        
        if now[1] < biggest:
            weight.append(now)
        else:
            count += 1
            if now[0] == m -1:
                print(count)
                return

case_num = int(sys.stdin.readline().strip())
for case in range(case_num):
    n, m = map(int, sys.stdin.readline().strip().split())
    weight = deque((idx, w) for idx, w in enumerate(map(int, sys.stdin.readline().strip().split())))
    printer_que(n, m+1, weight)