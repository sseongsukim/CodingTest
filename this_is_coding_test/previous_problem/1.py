"""
5
2 3 1 2 2
"""
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
group = 0
for a in arr:
    count += 1
    if a <= count:
        group += 1
        count = 0

print(group)