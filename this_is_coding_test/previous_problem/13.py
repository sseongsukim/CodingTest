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
houses = []
chickens = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[i][j] == 2:
            chickens.append((i, j))
        elif MAP[i][j] == 1:
            houses.append((i, j))

distance = int(1e9)
for case in list(combinations(chickens, M)):
    case_distance = 0
    for hx, hy in houses:
        temp = int(1e9)
        for cx, cy in case:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))

        case_distance += temp

    distance = min(distance, case_distance)

print(distance)
