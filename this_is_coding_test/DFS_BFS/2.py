"""
4 5
00110
00011
11111
00000

3 3
001
010
101
"""
N, M = map(int, input().split())

MAP = []
for i in range(N):
    MAP.append(list(map(int, input())))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def dfs(x, y):
    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 0:
                MAP[nx][ny] = 1
                dfs(nx, ny)

count = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)