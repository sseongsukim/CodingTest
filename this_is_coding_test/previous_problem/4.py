"""
5
3 2 1 1 9
"""
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

target = 1
for n in numbers:
    if target < n:
        break
    target += n

print(target)