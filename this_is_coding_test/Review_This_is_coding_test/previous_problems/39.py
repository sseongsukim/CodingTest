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
import sys
import heapq
input = sys.stdin.readline

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
INF = int(1e9)

T = int(input())
for _ in range(T):
    N = int(input())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, input().split())))

    distances = [[INF] * N for _ in range(N)]
    x, y = 0, 0
    distances[x][y] = MAP[x][y]
    q = []
    heapq.heappush(q, (distances[x][y], x, y))
    while q:
        dist, x, y = heapq.heappop(q)
        if distances[x][y] < dist:
            continue

        for d in range(4):
            dx = x + direction[d][0]
            dy = y + direction[d][1]
            if 0 <= dx < N and 0 <= dy < N:
                cost = dist + MAP[dx][dy]
                if cost < distances[dx][dy]:
                    distances[dx][dy] = cost
                    heapq.heappush(q, (cost, dx, dy))

    print(distances[N - 1][N - 1])
    