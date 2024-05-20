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

def union_parents(parents, x, y):
    x = find_parents(parents, x)
    y = find_parents(parents, y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

data = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))

data.sort()

answer = 0
for d in data:
    cost, x, y = d
    if find_parents(parents, x) != find_parents(parents, y):
        union_parents(parents, x, y)
        answer += cost

print(answer)
