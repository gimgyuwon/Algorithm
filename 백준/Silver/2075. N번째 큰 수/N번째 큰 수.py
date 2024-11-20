import heapq
import sys

def asscendingNumber(n):
    min_heap = []
    for _ in range (n):
        row = map(int, sys.stdin.readline().strip().split())
        for item in row:
            if len(min_heap) < n:
                heapq.heappush(min_heap, item)
            elif item > min_heap[0]:
                heapq.heappushpop(min_heap, item)
    return min_heap[0]


n = int(sys.stdin.readline().strip())
print(asscendingNumber(n))