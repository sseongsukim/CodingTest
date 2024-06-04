"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i

def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, x, y):
    x = find_parents(parents, x)
    y = find_parents(parents, y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[i][j] == 1:
            union_parents(parents, i + 1, j + 1)

tour_list = list(map(int, input().split()))
check = True
for i in range(len(tour_list) - 1):
    if find_parents(parents, tour_list[i]) != find_parents(parents, tour_list[i + 1]):
        check = False
        break

print("YES") if check else print("NO")