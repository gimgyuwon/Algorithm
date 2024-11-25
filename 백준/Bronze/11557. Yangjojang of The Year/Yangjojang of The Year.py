import sys
from collections import Counter

def solution(test_data):
    max_data = max(test_data, key=lambda x:int(x[1]))
    return max_data[0]

test_num = int(sys.stdin.readline().strip())
for _ in range(test_num):
    test_case_num = int(sys.stdin.readline().strip())
    test_data = [sys.stdin.readline().strip().split(" ") for _ in range(test_case_num)]
    print(solution(test_data))