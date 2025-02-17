"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1e9
MAP = [[INF] * (N + 1) for _ in range(N + 1)]

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if x == y:
            MAP[x][y] = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    if MAP[a][b] > cost:
        MAP[a][b] = cost

for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            MAP[x][y] = min(MAP[x][y], MAP[x][k] + MAP[k][y])

for x in range(1, N + 1):
    for y in range(1, N + 1):
        print(MAP[x][y], end=' ')
    print()