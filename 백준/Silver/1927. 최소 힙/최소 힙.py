import sys
import heapq

def min_heap(cmd_lst):
    heap = []
    for x in cmd_lst:
        if x == 0:
            print(heapq.heappop(heap) if heap else 0)
        else:
            heapq.heappush(heap, x)



cmd_num = int(sys.stdin.readline().strip())
cmd_lst = map(int, sys.stdin.read().splitlines())

min_heap(cmd_lst)