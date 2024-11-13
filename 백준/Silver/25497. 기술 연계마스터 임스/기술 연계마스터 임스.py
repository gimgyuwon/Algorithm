import sys
from collections import deque


def solution(data, N):
    dq = deque(data)
    tmp_dq = deque()
    skill_cnt = 0
    for _ in range(N):
        skill = dq.popleft()

        if skill.isdecimal():
            skill_cnt += 1

        elif skill == 'L':
            tmp_dq.append('L')

        elif skill == 'S':
            tmp_dq.append('S')

        elif skill == 'R':
            if 'L' in tmp_dq:
                tmp_dq.remove('L')
                skill_cnt += 1
            else:
                return skill_cnt

        elif skill == 'K':
            if 'S' in tmp_dq:
                tmp_dq.remove('S')
                skill_cnt += 1
            else:
                return skill_cnt

    return skill_cnt


n = int(sys.stdin.readline().strip())
input_data = sys.stdin.readline().strip()

print(solution(input_data, n))
