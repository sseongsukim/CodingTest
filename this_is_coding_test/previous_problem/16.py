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
from itertools import combinations
import copy
N, M = map(int, input().split())
arr = []
blank = []
virus = []
wall = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i, j))
        elif arr[i][j] == 1:
            wall.append((i, j))
        else:
            virus.append((i, j))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def spread(arr, x, y):
    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                spread(arr, nx, ny)

def count_blank(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1

    return count

arr_copy = copy.deepcopy(arr)
max_value = -1e9
for case in combinations(blank, 3):
    arr = copy.deepcopy(arr_copy)
    for new_wall in case:
        arr[new_wall[0]][new_wall[1]] = 1

    for vx, vy in virus:
        spread(arr, vx, vy)

    count = count_blank(arr)
    max_value = max(max_value, count)

print(max_value)
