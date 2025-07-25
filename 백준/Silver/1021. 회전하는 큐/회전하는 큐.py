import sys
from collections import deque


# rotate 양수는 뒤 -> 앞 / 음수는 앞 -> 뒤
def rotate_queue(idx_deq):
    op_num = 0
    for now in list(idx_deq):
        while num_lst[0] != now:
            if num_lst.index(now) > len(num_lst) // 2:
                num_lst.rotate(1)
            else:
                num_lst.rotate(-1)
            op_num += 1
        num_lst.popleft()
    return print(op_num)

max, num = map(int, sys.stdin.readline().strip().split())
lst = deque(range(1, max+1))
idx_deq = deque(map(int, sys.stdin.readline().strip().split()))
num_lst = deque(range(1, max+1))

rotate_queue(idx_deq)