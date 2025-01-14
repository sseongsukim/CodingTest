"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


INF = 1e9
distances = [INF] * (N + 1)
MAP = [[INF] * (N + 1) for _ in range(N + 1)]

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if x == y:
            MAP[x][y] = 0

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

start = 1
distances[start] = 0
q = []
heapq.heappush(q, (distances[start], start))
while q:
    dist, now = heapq.heappop(q)
    if distances[now] < dist:
        continue
    for next_node, next_dist in graph[now]:
        cost = dist + next_dist
        if cost < distances[next_node]:
            distances[next_node] = cost
            heapq.heappush(q, (cost, next_node))

max_distance = max(distances[1:])
number_of_node = distances[1:].count(max_distance)
for i in range(1, N + 1):
    if distances[i] == max_distance:
        minimum_idx = i
        break
print(minimum_idx, max_distance, number_of_node)