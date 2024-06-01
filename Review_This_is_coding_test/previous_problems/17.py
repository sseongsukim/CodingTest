"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
-> 3
3 3
1 0 2
0 0 0
3 0 0
1 2 2
-> 0
"""
from collections import deque
N, K = map(int, input().split())
MAP = []
data = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[i][j] != 0:
            data.append((MAP[i][j], 0, i, j))
S, X, Y = map(int, input().split())
data.sort()

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]

q = deque(data)
while q:
    number, s, x, y = q.popleft()
    if s == S:
        break

    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < N:
            if MAP[nx][ny] == 0:
                MAP[nx][ny] = number
                q.append((number, s + 1, nx, ny))

print(MAP[X - 1][Y - 1])