"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
TC = int(input())
for _ in range(TC):
    N = int(input())
    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))

    distance = [[INF] * (N + 1) for _ in range(N + 1)]
    x, y = 0, 0
    distance[x][y] = MAP[x][y]
    heap = []
    heapq.heappush(heap, (distance[x][y], x, y))
    while heap:
        dist, x, y = heapq.heappop(heap)
        if dist < distance[x][y]:
            continue

        for d in range(4):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + MAP[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(heap, (distance[nx][ny], nx, ny))

    print(distance[N - 1][N - 1])