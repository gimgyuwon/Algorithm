import heapq

def solution(scoville, K):
    answer = 0
    # 1. 기존 리스트를 힙으로 변환 (O(N))
    heapq.heapify(scoville)
    
    # 2. 가장 작은 값이 K보다 작을 때까지만 반복
    while scoville[0] < K:
        # 모든 음식을 다 섞었는데도 K 미만인 경우 (더 이상 섞을 게 없음)
        if len(scoville) < 2:
            return -1
        
        # 3. 가장 맵지 않은 두 개 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 4. 새로운 음식 만들기
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
        
    return answer