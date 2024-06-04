"""
4
3
4
1
1
->2
4
6
2
2
3
3
4
4
-> 3
"""
import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

parents = [0] * (G + 1)
for i in range(1, G + 1):
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

count = 0
for _ in range(P):
    number = int(input())
    parent = find_parents(parents, number)
    if parent == 0:
        break
    union_parents(parents, parent, parent - 1)
    count += 1

print(count)