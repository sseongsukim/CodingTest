"""
4 4 2 1
1 2
1 3
2 3
2 4
-> 4

4 3 2 1
1 2
1 3
1 4
-> -1

4 4 1 1
1 2
1 3
2 3
2 4
-> 2 3
"""
from collections import deque
N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [0] * (N + 1)
visited = [False] * (N + 1)
distance[start] = 0
visited[start] = True
q = deque()
q.append(start)
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if not visited[next_node]:
            distance[next_node] = distance[now] + 1
            visited[next_node] = True
            q.append(next_node)

if K not in distance[1:]:
    print(-1)
else:
    for i in range(1, N + 1):
        if distance[i] == K:
            print(i)