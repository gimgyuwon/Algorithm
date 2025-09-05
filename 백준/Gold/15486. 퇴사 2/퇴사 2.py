import sys



def termination(n):
    for i in range(n, 0, -1):
        if i + time[i] <= n + 1:
            dp[i] = max(price[i] + dp[i + time[i]], dp[i+1])
        else:
            dp[i] = dp[i+1]
    return dp[1]

data = sys.stdin.read().splitlines()
n = int(data[0])
time = [0] * (n+1)
price = [0] * (n+1)
dp = [0] * (n+2)

for i in range(1, n+1):
    t, p = map(int, data[i].split())
    time[i] = t
    price[i] = p



print(termination(n))