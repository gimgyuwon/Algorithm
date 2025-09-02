import sys

input = sys.stdin.readline

def sticker(n, first_row, second_row):
    arr = [first_row, second_row]
    dp = [[0]*n for _ in range(2)]

    if n == 0:
        return 0
    elif n == 1:
        return max(arr[0][0], arr[1][0])

    # 0번째 열
    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

    # 1번째 열
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]

    for x in range(2, n):
        # 2번째 열 이상
        dp[0][x] = max(dp[1][x-1], dp[1][x-2]) + arr[0][x]
        dp[1][x] = max(dp[0][x-1], dp[0][x-2]) + arr[1][x]

    return max(dp[0][n-1], dp[1][n-1])

case_n = int(input())
for _ in range(case_n):
    n = int(input())
    first_row = list(map(int, input().strip().split()))
    second_row = list(map(int, input().strip().split()))
    print(sticker(n, first_row, second_row))