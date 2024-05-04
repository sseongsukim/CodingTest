"""
3 2 1
1 2 4
1 3 2
"""
import heapq
import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next_node in graph[now]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(heap, (cost, next_node[0]))

dijkstra(C)

count = 0
max_value = 0
for d in distance:
    if d != INF:
        count += 1
        max_value = max(max_value, d)

print(count - 1, max_value)