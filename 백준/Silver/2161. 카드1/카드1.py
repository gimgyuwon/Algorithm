import sys
from collections import deque


def solution(input_data):
    ans = []
    dq = deque(list(range(1, input_data+1)))
    for _ in range(len(dq)):
        ans.append(dq.popleft())
        if len(ans) != input_data:
            tmp = dq.popleft()
            dq.append(tmp)

    return str(ans)[1:-1].replace(",", "")


input_data = int(sys.stdin.readline().strip())
print(solution(input_data))
