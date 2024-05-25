"""
5
3 2 1 1 9
"""
N = int(input())
arr = sorted(list(map(int, input().split())))
target = 1
for a in arr:
    if target < a:
        break
    target += a

print(target)