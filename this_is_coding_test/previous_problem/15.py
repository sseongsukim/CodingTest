"""
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
"""
from collections import deque
N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

distance = [0] * (N + 1)
visited = [False] * (N + 1)
distance[X] = 0
visited[X] = True
q = deque()
q.append(X)
while q:
    now = q.popleft()
    for next_node in arr[now]:
        if not visited[next_node]:
            distance[next_node] = distance[now] + 1
            visited[next_node] = True
            q.append(next_node)

for i in range(1, N + 1):
    if distance[i] == K:
        print(i)

if K not in distance[1:]:
    print(-1)