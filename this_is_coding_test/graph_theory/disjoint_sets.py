"""
6 4
1 4
2 3
2 4
5 6
"""
N, M = map(int, input().split())
parents = [0] * (N + 1)

for i in range(1, N + 1):
    parents[i] = i

def find_parents(parents, x):
    if parents[x] != x:
        return find_parents(parents, parents[x])
    return x

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    union_parents(parents, a, b)

for i in range(N + 1):
    print(find_parents(parents, i), end= ' ')

print()
print(parents[1:], end= ' ')