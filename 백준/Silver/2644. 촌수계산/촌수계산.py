import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
# 부모는 항상 자식보다 숫자가 작다
parent, child = map(int, sorted(data[1].split()))
m = int(data[2])

lst = [list(map(int, part.split())) for part in data[3:]]

graph = defaultdict(list)

for x, y in lst:
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, node, goal, n):
    visited = [False] * (n+1)
    stack = [(node, 0)]

    while stack:
        node, cnt = stack.pop()

        if node == goal:
            return cnt
        
        if not visited[node]:
            visited[node] = True
            for child in reversed(graph[node]):
                if not visited[child]:
                    stack.append((child, cnt+1))
    return -1


print(dfs(graph, parent, child, n))