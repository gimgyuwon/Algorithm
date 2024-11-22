import sys
import heapq


def solution(k, num_list):
    heapq.heapify(num_list)
    for _ in range(int(k)-1):
        heapq.heappop(num_list)
    return heapq.heappop(num_list)


input_data = sys.stdin.readline().strip()
num, k = input_data.split()
num_list = list(map(int, sys.stdin.readline().strip().split()))

print(solution(k, num_list))