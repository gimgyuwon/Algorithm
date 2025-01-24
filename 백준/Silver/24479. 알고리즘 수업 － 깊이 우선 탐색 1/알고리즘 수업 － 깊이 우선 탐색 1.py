import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(graph, node, visited, seq, order):
    visited[node] = True
    seq[node] = order[0]
    order[0] += 1
    for neighbor in sorted(graph[node]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, seq, order)

data = input().splitlines()
n, m, r = map(int, data[0].split())
edges = data[1:]

graph = defaultdict(list)
for edge in edges:
    u, v = map(int, edge.split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
seq = [0] * (n + 1)
order = [1]

dfs(graph, r, visited, seq, order)

sys.stdout.write("\n".join(map(str, seq[1:])) + "\n")
