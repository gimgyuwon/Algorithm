import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
parent, child = map(int, sorted(data[1].split()))
m = int(data[2])
lst = [list(map(int, line.split())) for line in data[3:]]

# 무방향 그래프
graph = [[] for _ in range(n+1)]
for x, y in lst:
    graph[x].append(y)
    graph[y].append(x)

# 부모는 항상 자식 보다 번호가 작음
def bfs(graph, start, goal, n):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        node, cnt = queue.popleft()

        if node == goal:
            return cnt

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cnt + 1))
    return -1


print(bfs(graph, parent, child, n))
