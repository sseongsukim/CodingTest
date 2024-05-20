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

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

max_value = -1e9
total_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b):
        union_parents(parents, a, b)
        total_cost += cost
        max_value = cost

print(total_cost - max_value)