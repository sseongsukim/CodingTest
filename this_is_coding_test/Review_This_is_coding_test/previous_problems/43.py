import sys
input = sys.stdin.readline
N, M = map(int, input().split())

parents = [0] * N
for i in range(1, N):
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
total_cost = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))
    total_cost += cost
data.sort(key=lambda x: x[0])

used_cost = 0
for cost, x, y in data:
    if find_parents(parents, x) != find_parents(parents, y):
        union_parents(parents, x, y)
        used_cost += cost

print(total_cost - used_cost)
