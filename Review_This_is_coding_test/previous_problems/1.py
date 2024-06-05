"""
5
2 3 1 2 2
"""
N = int(input())
numbers = sorted(list(map(int, input().split())))

group = 0
number = 0
for n in numbers:
    number += 1
    if number == n:
        group += 1
        number = 0

print(group)