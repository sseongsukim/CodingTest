"""
5
2 3 1 2 2
"""
N = int(input())
arr = sorted(list(map(int, input().split())))

group = 0
count = 0
for a in arr:
    count += 1
    if count >= a:
        group += 1
        count = 0

print(group)