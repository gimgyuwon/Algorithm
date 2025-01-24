import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.read
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

def bfs(graph, node, visited, seq):
    order = 1
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            seq[node] = order
            order += 1

            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    queue.append(neighbor)

bfs(graph, r, visited, seq)
sys.stdout.write("\n".join(map(str, seq[1:])) + "\n")
