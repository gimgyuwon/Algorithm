import sys


def solution(input_data):
    ans = []
    for i in input_data:
        if i not in ans:
            ans.append(i)
    if len(ans) >= (len(input_data)//2):
        return len(input_data)//2
    return len(ans)


input_data = str(sys.stdin.readline().strip())
input_data = list(input_data[1:-1].split(","))

print(solution(input_data))

# print(input_data)
