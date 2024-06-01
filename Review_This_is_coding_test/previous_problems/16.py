"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
-> 27
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
-> 9
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
-> 3
"""
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = []
viruses = []
walls = []
blanks = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(M):
        if MAP[i][j] == 2:
            viruses.append((i, j))
        elif MAP[i][j] == 1:
            walls.append((i, j))
        else:
            blanks.append((i, j))

def count_zero(NMAP):
    zero_count = 0
    for i in range(N):
        for j in range(M):
            if NMAP[i][j] == 0:
                zero_count += 1
    return zero_count

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def spread(MAP, x, y):
    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 0:
                MAP[nx][ny] = 2
                spread(MAP, nx, ny)

count = -1e9
for case in list(combinations(blanks, 3)):
    NMAP = copy.deepcopy(MAP)
    for wx, wy in case:
        NMAP[wx][wy] = 1

    for vx, vy in viruses:
        spread(NMAP, vx, vy)

    zero_count = count_zero(NMAP)

    count = max(count, zero_count)

print(count)
