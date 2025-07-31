import sys
import heapq

def absolute_heap(cmd_lst):
    abs_hp = []
    for x in cmd_lst:
        if x == 0:
            print(heapq.heappop(abs_hp)[1] if abs_hp else 0)
        else:
            heapq.heappush(abs_hp, (abs(x), x))
    return


cmd_lst = map(int, sys.stdin.read().splitlines()[1:])

absolute_heap(cmd_lst)