"""
4
3
4
1
1

4
6
2
2
3
3
4
4
"""
import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
parents = [0] * (G + 1)
for i in range(G + 1):
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

count = 0
for _ in range(P):
    number = int(input())
    parent = find_parents(parents, number)
    if parent == 0:
        break
    union_parents(parents, parent, parent - 1)
    count += 1

print(count)