from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
for x, y in list(combinations(numbers, 2)):
    if x != y:
        count += 1
print(count)