import sys
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        part = heapq.heappop(scoville)
        if part >= K:
            return answer
        if len(scoville) == 0:
            return -1
        new_part = part + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new_part)
        answer += 1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
