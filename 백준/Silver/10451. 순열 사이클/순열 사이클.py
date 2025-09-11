import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node, lst, visited):
    visited[node] = True
    next = lst[node]
    if not visited[next]:
        dfs(next, lst, visited)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        data = list(map(int, input().split()))
        lst = [0] + data
        visited = [False] * (n+1)
        count = 0

        for i in range(1, n+1):
            if not visited[i]:
                dfs(i, lst, visited)
                count += 1
        
        print(count)


if __name__ == "__main__":
    main()