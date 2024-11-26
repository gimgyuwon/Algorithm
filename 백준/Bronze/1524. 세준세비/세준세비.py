import heapq
import sys
import heapq

def solution():
    test_case = int(sys.stdin.readline().strip())
    for _ in range(test_case):
        sys.stdin.readline()
        sz_qty, sb_qty = sys.stdin.readline().strip().split(" ")
        sz_strength = list(map(int, sys.stdin.readline().strip().split(" ")))
        sb_strength = list(map(int, sys.stdin.readline().strip().split(" ")))
        heapq.heapify(sz_strength)
        heapq.heapify(sb_strength)

        while sz_strength and sb_strength:
            if sz_strength[0] >= sb_strength[0]:
                heapq.heappop(sb_strength)
            else:
                heapq.heappop(sz_strength)

        if not sz_strength:
            print("B")
        elif not sb_strength:
            print("S")
    return 0

solution()