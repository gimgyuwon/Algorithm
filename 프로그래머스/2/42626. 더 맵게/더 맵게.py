import sys
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    part = heapq.heappop(scoville)
    while part < K:
        if len(scoville) == 0:
            return -1
        new_part = part + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new_part)
        part = heapq.heappop(scoville)
        answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
