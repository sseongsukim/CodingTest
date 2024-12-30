"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
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

for _ in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parents(parents, a, b)
    else:
        if find_parents(parents, a) != find_parents(parents, b):
            print("NO")
        else:
            print("YES")