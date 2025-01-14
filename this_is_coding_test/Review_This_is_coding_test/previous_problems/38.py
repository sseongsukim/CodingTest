"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e9
MAP = [[INF] * (N + 1) for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, N + 1):
        if x == y:
            MAP[x][y] = 0

for _ in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = 1

for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            MAP[x][y] = min(MAP[x][y], MAP[x][k] + MAP[k][y])

answer = 0
for x in range(1, N + 1):
    count = 0
    for y in range(1, N + 1):
        if MAP[x][y] != INF or MAP[y][x] != INF:
            count += 1
    if count == N:
        answer += 1
print(answer)