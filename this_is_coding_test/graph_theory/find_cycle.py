"""
3 3
1 2
1 3
2 3
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

cycle = False
for i in range(M):
    a, b = map(int, input().split())
    if find_parents(parents, a) == find_parents(parents, b):
        cycle = True
        break
    else:
        union_parents(parents, a, b)

if cycle:
    print('Cycle')
else:
    print('No')