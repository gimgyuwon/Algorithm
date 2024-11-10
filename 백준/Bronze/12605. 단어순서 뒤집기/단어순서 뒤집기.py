import sys


def solution(input_data):
    for i, part in enumerate(input_data, start=1):
        print(f"Case #{i}: {' '.join(part[::-1])}")


input_num = int(sys.stdin.readline().strip())
input_data = [sys.stdin.readline().strip().split() for _ in range(input_num)]

solution(input_data)
