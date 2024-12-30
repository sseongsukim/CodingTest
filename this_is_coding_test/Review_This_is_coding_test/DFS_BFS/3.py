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
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if MAP[x][y] == 0:
        MAP[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)