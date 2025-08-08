import sys

def longest_decreasing_subsequence(n, seq):
    dp = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if seq[i] < seq[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().strip().split()))

print(max(longest_decreasing_subsequence(n, seq)))