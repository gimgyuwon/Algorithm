import sys
from collections import defaultdict, deque

input = sys.stdin.read


inp = input().splitlines()
n, m, v = map(int, inp[0].split())
edges = [tuple(map(int, part.split())) for part in inp[1:]]

graph = defaultdict(list)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node].sort()

dfs_result = []
bfs_result = []

def dfs(graph, v, visited):
    visited[v] = True
    dfs_result.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    return dfs_result

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    bfs_result = [start]
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                bfs_result.append(neighbor)
    return bfs_result

print(*dfs(graph, v, visited=[False]*(n+1)))
print(*bfs(graph, v, visited=[False]*(n+1)))