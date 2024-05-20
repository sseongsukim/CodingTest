"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
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

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

total_cost = 0
data = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))
    total_cost += cost
data.sort()

used_cost = 0
for d in data:
    cost, x, y = d
    if find_parents(parents, x) != find_parents(parents, y):
        union_parents(parents, x, y)
        used_cost += cost

print(total_cost)
print(used_cost)
print(total_cost - used_cost)