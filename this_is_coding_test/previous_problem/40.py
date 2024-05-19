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
    distance[start] = 0
    q = []
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node in arr[now]:
            cost = dist + next_node[1]
            if distance[next_node[0]] > cost:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))

dijkstra(1)
print(distance)