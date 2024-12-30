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
stores = []
for x in range(N):
    MAP.append(list(map(int, input().split())))
    for y in range(N):
        if MAP[x][y] == 1:
            houses.append((x, y))
        elif MAP[x][y] == 2:
            stores.append((x, y))

answer = 1e9
for case in list(combinations(stores, M)):
    total_distance = 0
    for hx, hy in houses:
        distance = 1e9
        for cx, cy in case:
            distance = min(distance, abs(hx - cx) + abs(hy - cy))
        total_distance += distance
    answer = min(answer, total_distance)
print(answer)