import sys
sys.setrecursionlimit(10**6)

def dfs(graph, node, visited, seq, order):
    visited[node] = True
    seq[node] = order[0]
    order[0] += 1
    for i in sorted(graph[node]):
        if not visited[i]:
            dfs(graph, i, visited, seq, order)
    return seq


n, m, r = map(int, sys.stdin.readline().strip().split(" "))
edges = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(m)]
graph = [[] for _ in range(n+1)]

for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
seq = [0] * (n+1)
order = [1]

dfs(graph, r, visited, seq, order)

for i in range(1, n+1):
    print(seq[i])