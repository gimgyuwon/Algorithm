import sys
from collections import defaultdict, deque

input = sys.stdin.read

def build_graph(edges, n):
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for node in range(1, n+1):
        graph[node].sort()
    return graph

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def find_connected_components(graph, n):
    cc = 0
    visited = [False] * (n+1)

    for node in range(1, n+1):
        if not visited[node]:
            bfs(graph, node, visited)
            cc += 1
    return cc


def main():
    inp = input().splitlines()
    n, m = map(int, inp[0].split())
    edges = [tuple(map(int, part.split())) for part in inp[1:]]
    graph = build_graph(edges, n)
    print(find_connected_components(graph, n))

if __name__ == "__main__":
    main()