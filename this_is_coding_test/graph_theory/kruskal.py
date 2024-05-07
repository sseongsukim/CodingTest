"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
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

total_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b):
        union_parents(parents, a, b)
        total_cost += cost

print(total_cost)