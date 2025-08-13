import sys

def ascent_num(n):
    dp = [[0]*10 for _ in range (n)]
    for x in range(10):
        dp[0][x] = 1
    for y in range(n):
        dp[y][0] = 1

    for y in range(1, n):
        for x in range(1, 10):
            dp[y][x] = dp[y-1][x] + dp[y][x-1]
    return sum(dp[n-1]) % 10007

n = int(sys.stdin.readline().strip())
print(ascent_num(n))