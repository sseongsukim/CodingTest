"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""
import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline
N, M = map(int, input().split())
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
MAP = []
blank = []
wall = []
virus = []
for x in range(N):
    MAP.append(list(map(int, input().split())))
    for y in range(M):
        if MAP[x][y] == 2:
            virus.append((x, y))
        elif MAP[x][y] == 0:
            blank.append((x, y))


def bfs(MAP, x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for d in range(4):
            dx = x + direction[d][0]
            dy = y + direction[d][1]
            if 0 <= dx < N and 0 <= dy < M and MAP[dx][dy] == 0:
                MAP[dx][dy] = 2
                q.append((dx, dy))
    return MAP

def count_blank(MAP):
    count = 0
    for x in range(N):
        for y in range(M):
            if MAP[x][y] == 0:
                count += 1
    return count

answer = -1e9
for case in list(combinations(blank, 3)):
    COPYMAP = copy.deepcopy(MAP)
    for cx, cy in case:
        COPYMAP[cx][cy] = 1
    for vx, vy in virus:
        bfs(COPYMAP, vx, vy)
    count = count_blank(COPYMAP)
    answer = max(answer, count)
print(answer)