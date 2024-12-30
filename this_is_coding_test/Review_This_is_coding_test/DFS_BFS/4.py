"""
5 6
101010
111111
000001
111111
111111
"""
from collections import deque

N, M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input())))

x, y = 0, 0
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
q = deque()
q.append((x, y))
while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 1:
                MAP[nx][ny] = MAP[x][y] + 1
                q.append((nx, ny))

print(MAP[N - 1][M - 1])