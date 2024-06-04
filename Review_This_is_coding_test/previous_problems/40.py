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
INF = int(1e9)

MAP = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    MAP[a].append(b)
    MAP[b].append(a)

start = 1
distance = [INF] * (N + 1)
visited = [False] * (N + 1)

distance[start] = 0
visited[start] = True

heap = []
heapq.heappush(heap, (distance[start], start))

while heap:
    dist, now = heapq.heappop(heap)
    if dist < distance[now]:
        continue
    for next_node in MAP[now]:
        if not visited[next_node]:
            cost = dist + 1
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (distance[next_node], next_node))

max_distance = max(distance[1:])
count = 0
indices = []
for i in range(1, N + 1):
    if distance[i] == max_distance:
        count += 1
        indices.append(i)

print(min(indices), end= ' ')
print(max_distance, end= ' ')
print(count, end= ' ')
