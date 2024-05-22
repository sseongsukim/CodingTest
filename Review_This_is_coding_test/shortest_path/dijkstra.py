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
N, M = map(int, input().split())
start = int(input())
data = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    data[a].append((b, cost))

INF = int(1e9)
distance = [INF] * (N + 1)
distance[start] = 0
q = []
heapq.heappush(q, (distance[start], start))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for next_node, next_cost in data[now]:
        cost = dist + next_cost
        if distance[next_node] > cost:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

print(distance[1:])