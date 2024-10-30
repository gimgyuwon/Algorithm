from collections import deque

def solution(s):
    ans = 0
    q = deque(s)
    
    while q:
        a, b = 1, 0
        x = q.popleft()
        
        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
        else:
            # q가 비어 있고 a != b 인 경우 마지막으로 추가
            if a != b:
                ans += 1

    return ans
