import sys

input = sys.stdin.readline

def calc_ox_score(ans_lst):
    score = 0
    stack = 0
    for ans in ans_lst:
        if ans == 'O':
            stack += 1
            score += stack
        else:
            stack = 0
    return score

n = int(input())
for _ in range(n):
    print(calc_ox_score(list(input())))