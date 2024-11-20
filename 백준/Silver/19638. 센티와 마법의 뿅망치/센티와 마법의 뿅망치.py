import sys
import heapq

def magic_hammer(giants, myHeight, limit):
    heapq.heapify(giants)
    usage = 0
    for _ in range(limit):
        max_height = -giants[0]
        if myHeight > max_height:
            break
        if max_height == 1:
            break
        new_height = max_height // 2
        heapq.heapreplace(giants, -new_height)  # 최댓값을 반으로 줄인 후 업데이트
        usage += 1

    max_height = -giants[0]  # 가장 큰 거인의 키 확인
    if myHeight > max_height:
        print("YES")
        print(usage)
    else:
        print("NO")
        print(max_height)

population, myHeight, limit = map(int, sys.stdin.readline().strip().split())
giants = [-int(sys.stdin.readline().strip()) for _ in range(population)]

magic_hammer(giants, myHeight, limit)
