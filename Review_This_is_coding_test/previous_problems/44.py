"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
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

x = []
y = []
z = []
for i in range(N):
    coordinate = list(map(int, input().split()))
    x.append((coordinate[0], i))
    y.append((coordinate[1], i))
    z.append((coordinate[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()
answer = 0
for cost, x, y in edges:
    if find_parents(parents, x) != find_parents(parents, y):
        union_parents(parents, x, y)
        answer += cost

print(answer)