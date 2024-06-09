"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
"""
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

MAP = []
house = []
chicken = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[i][j] == 1:
            house.append((i, j))
        elif MAP[i][j] == 2:
            chicken.append((i, j))

min_distance = 1e9
for case in list(combinations(chicken, M)):
    case_distance = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in case:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        case_distance += tmp
    min_distance = min(min_distance, case_distance)
print(min_distance)