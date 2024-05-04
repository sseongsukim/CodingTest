# Dijkstra
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start))
    while heap:
        # print(heap)
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next_node in graph[now]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(heap, (cost, next_node[0]))

dijkstra(start)
print(distance)