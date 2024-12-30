"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
N, M = map(int, input().split())
parents = [0] * (N + 1)
for i in range(N + 1):
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


data = []
for i in range(M):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))
data.sort()
total = 0
last = 0
for cost, x, y in data:
    if find_parents(parents, x) != find_parents(parents, y):
        union_parents(parents, x, y)
        total += cost
        last = cost

print(total - last)