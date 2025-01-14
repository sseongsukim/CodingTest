w
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
T = int(input())
for i in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = arr[0][0]
    q = []
    heapq.heappush(q, (distance[0][0], 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for d in range(4):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + arr[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (distance[nx][ny], nx, ny))

    print(distance[N-1][N-1])
