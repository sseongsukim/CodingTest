"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""
from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
alls = list(combinations(arr, 2))
count = 0
for x, y in alls:
    if x != y:
        count += 1

print(count)
