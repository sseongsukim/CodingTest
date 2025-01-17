"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
import sys
input = sys.stdin.readline

N = int(input())
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

xs = []
ys = []
zs = []
for i in range(N):
    x, y, z = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))

xs.sort()
ys.sort()
zs.sort()

edges = []
for i in range(N - 1):
    edges.append((xs[i + 1][0] - xs[i][0], xs[i][1], xs[i + 1][1]))
    edges.append((ys[i + 1][0] - ys[i][0], ys[i][1], ys[i + 1][1]))
    edges.append((zs[i + 1][0] - zs[i][0], zs[i][1], zs[i + 1][1]))

edges.sort()
answer = 0
for cost, x, y in edges:
    if find_parents(parents, x) != find_parents(parents, y):
        union_parents(parents, x, y)
        answer += cost

print(answer)