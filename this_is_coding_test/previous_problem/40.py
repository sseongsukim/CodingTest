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
INF = int(1e9)
N, M = map(int, input().split())
distance = [INF] * (N + 1)
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append((b, 1))
    arr[b].append((a, 1))


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next_node in arr[now]:
            cost = next_node[1] + dist
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(heap, (cost, next_node[0]))

dijkstra(1)
nodes = []
max_values = -INF
for i in range(1, N + 1):
    if max_values < distance[i]:
        max_values = distance[i]
        max_value_indices = [i]
    else:
        max_value_indices.append(i)

print(min(max_value_indices), max_values, len(max_value_indices))