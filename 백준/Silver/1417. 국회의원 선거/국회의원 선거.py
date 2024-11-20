import sys


def vote(input_data):
    ans = 0
    candi = input_data.pop(0)
    if len(input_data) == 0:
        return 0
    if candi == max(input_data):
        return 1
    while candi <= max(input_data):
        rival = max(input_data)
        if candi <= rival:
            input_data[input_data.index(rival)] = rival-1
            candi += 1
            ans += 1

    return ans


n = int(sys.stdin.readline().strip())
input_data = [int(sys.stdin.readline().strip()) for _ in range(n)]

print(vote(input_data))
