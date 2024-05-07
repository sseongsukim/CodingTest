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
import sys
input = sys.stdin.readline
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

for _ in range(M):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union_parents(parents, a, b)
    elif operator == 1:
        if find_parents(parents, a) != find_parents(parents, b):
            print('NO')
        else:
            print('YES')