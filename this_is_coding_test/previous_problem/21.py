"""
2 20 50
50 30
20 40

2 40 50
50 30
20 40

2 20 50
50 30
30 40

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
"""
from collections import deque
N, L, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def bfs(x, y, index):
    united = [(x, y)]
    summations = arr[x][y]
    count = 1
    union[x][y] = index
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    union[nx][ny] = index
                    united.append((nx, ny))
                    summations += arr[nx][ny]
                    count += 1
                    q.append((nx, ny))

    for ux, uy in united:
        arr[ux][uy] = summations // count

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