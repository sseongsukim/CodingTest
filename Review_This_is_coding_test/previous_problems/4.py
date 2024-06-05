"""
5
3 2 1 1 9
-> 8
"""
N = int(input())
numbers = sorted(list(map(int, input().split())))

target = 1
for n in numbers:
    if target < n:
        break
    else:
        target += n

print(target)