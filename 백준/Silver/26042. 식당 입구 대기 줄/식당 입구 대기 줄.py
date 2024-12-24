import sys
from collections import deque

def solution(N, data):
    line = []
    max_line  = 0
    result = []

    for item in data:
        action = int(item[0])
        a = item[1] if len(item) > 1 else None
        if action == 1:
            line.append(a)
        elif action == 2:
            if line:
                line.pop()
        if max_line <= len(line):
            max_line = len(line)
            last_std = line[-1] if line else None
            result.append([max_line, last_std])

    filtered = [arg for arg in result if arg[0] == max_line]
    result = min(filtered, key=lambda x: int(x[1]))

    return f"{result[0]} {result[1]}"


n = int(sys.stdin.readline().strip())
input_data = [sys.stdin.readline().strip().split(" ") for _ in range(n)]
print(solution(n, input_data))