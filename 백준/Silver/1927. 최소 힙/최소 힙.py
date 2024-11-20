import sys
import heapq


def minOperation(data):
    min_heap = []

    for part in data:
        if part == 0:
            if min_heap:
                print(heapq.heappop(min_heap))
            else:
                print(0)
        else:
            heapq.heappush(min_heap, part)

n = int(sys.stdin.readline().strip())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]

minOperation(data)
