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

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def dfs(x, y):
    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                dfs(nx, ny)

count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)
