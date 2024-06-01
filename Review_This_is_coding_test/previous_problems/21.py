"""
2 20 50
50 30
20 40
-> 1

2 40 50
50 30
20 40
-> 0

2 20 50
50 30
30 40
-> 1

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
-> 3
"""
from collections import deque
N, L, R = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def bfs(x, y, index):
    united = [(x, y)]
    number = 1
    summation = MAP[x][y]
    union[x][y] = index
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(MAP[nx][ny] - MAP[x][y]) <= R:
                    number += 1
                    summation += MAP[nx][ny]
                    q.append((nx, ny))
                    united.append((nx, ny))
                    union[nx][ny] = index
    for ux, uy in united:
        MAP[ux][uy] = int(summation / number)

count = 0
while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == N * N:
        break

    count += 1

print(count)
