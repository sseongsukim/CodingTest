"""
5 3
1
2
8
4
9
"""
N, C = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()

start = 1
end = numbers[-1] - numbers[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    value = numbers[0]
    count = 1
    for i in numbers[1:]:
        if value + mid <= i:
            count += 1
            value = i

    if count < C:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)


