import sys

n, m= map(int, sys.stdin.readline().strip().split())

used = [False] * (n + 1)
result = []

def backtrack(depth):
    if (depth == m):
        print(*result)    
        return

    for num in range(1, n+1):
        if not used[num]:
            used[num] = True
            result.append(num)    

            backtrack(depth+1)

            result.pop()
            used[num] = False

backtrack(0)