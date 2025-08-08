import sys

input = sys.stdin.readline

def longest_increasing_subsequence(n, seq):
    dp = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[j]+1, dp[i])
    return dp

n = int(input())
seq = list(map(int, input().strip().split()))

print(max(longest_increasing_subsequence(n, seq)))