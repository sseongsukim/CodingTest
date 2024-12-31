"""
4 4 2 1
1 2
1 3
2 3
2 4
"""
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distances = [0] * (N + 1)
visited = [False] * (N + 1)
visited[X] = True
q = deque()
q.append(X)
while q:
    now = q.popleft()
    visited[now] = True
    for next_node in graph[now]:
        if not visited[next_node]:
            distances[next_node] = distances[now] + 1
            visited[next_node] = True
            q.append(next_node)
for i, dist in enumerate(distances[1:]):
    if dist == K:
        print(i + 1)