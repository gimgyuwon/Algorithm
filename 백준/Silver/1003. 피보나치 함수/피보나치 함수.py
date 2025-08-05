import sys

def fibonacci_cnt(n):
    zero = [1, 0] + [0] * (n-1)
    one = [0, 1] + [0] * (n-1)

    for i in range(2, n+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i - 1] + one[i - 2]
    return zero[n], one[n]

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    print(*fibonacci_cnt(int(input())))
