"""
5 3
1
2
8
4
9
"""
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()

start = 1
end = numbers[-1] - numbers[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    value = numbers[0]
    count = 1
    for n in numbers[1:]:
        if n >= mid + value:
            value = n
            count += 1

    if count < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)