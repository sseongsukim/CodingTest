"""
3 2 1
1 2 4
1 3 2
"""
import heapq
N, M, C = map(int, input().split())
INF = int(1e9)
data = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, cost = map(int, input().split())
    data[a].append((cost, b))

distance = [INF] * (N + 1)
distance[C] = 0
q = []
heapq.heappush(q, (distance[C], C))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for next_cost, next_node in data[now]:
        cost = dist + next_cost
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

count = 0
max_distance = 0
for d in distance[1:]:
    if d != INF and d != 0:
        count += 1
        max_distance = max(max_distance, d)

print(count, max_distance)
