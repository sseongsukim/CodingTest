"""
5 3
1 3 2 3 2
-> 8
8 5
1 5 4 3 2 4 5 2
-> 25
"""
from itertools import combinations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
for case in list(combinations(numbers, 2)):
    if case[0] != case[1]:
        count += 1

print(count)