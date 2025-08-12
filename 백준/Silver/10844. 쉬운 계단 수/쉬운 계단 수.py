import sys

def easy_num_of_stairs(n):
    dp = [[0]*10 for _ in range(n+1)]

    for i in range(1, 10):
        dp[1][i] = 1

    for y in range(2, n+1):
        for x in range(10):
            if x == 0:
                dp[y][x] = dp[y-1][1]
            elif x == 9:
                dp[y][x] = dp[y-1][8]
            else:
                dp[y][x] = dp[y-1][x-1] + dp[y-1][x+1]

    return sum(dp[n]) % 1000000000

n = int(sys.stdin.readline().strip())
print(easy_num_of_stairs(n))