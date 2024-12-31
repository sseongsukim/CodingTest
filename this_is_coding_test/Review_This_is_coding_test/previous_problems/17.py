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
import sys
input = sys.stdin.readline

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, K = map(int, input().split())
MAP = []
viruses = []

for x in range(N):
    MAP.append(list(map(int, input().split())))
    for y in range(N):
        if MAP[x][y] != 0:
            viruses.append((MAP[x][y], 0, x, y))
viruses.sort(key= lambda x: x[0])
q = deque(viruses)

S, X, Y = map(int, input().split())
while q:
    number, time, x, y = q.popleft()
    if time == S:
        break
    for d in range(4):
        dx = x + direction[d % 4][0]
        dy = y + direction[d % 4][1]
        if 0 <= dx < N and 0 <= dy < N and MAP[dx][dy] == 0:
            MAP[dx][dy] = number
            q.append((MAP[dx][dy], time + 1, dx, dy))

print(MAP[X - 1][Y - 1])