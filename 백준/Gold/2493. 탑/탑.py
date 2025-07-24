import sys

def who_get_laser(top_num, top_heights):
    stack = []
    result = [0] * top_num

    for i in range(top_num):
        while stack and top_heights[stack[-1]] < top_heights[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

    print(' '.join(map(str, result)))


top_num = int(sys.stdin.readline())
top_heights = list(map(int, sys.stdin.readline().split()))
who_get_laser(top_num, top_heights)
