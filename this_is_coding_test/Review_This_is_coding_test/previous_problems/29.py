N, C = map(int, input().split())
numbers = []
for _ in range(N):
    n = int(input())
    numbers.append(n)

numbers.sort()

start = 1
end = numbers[-1] - numbers[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    idx = 0
    for i in range(1, N):
        if (numbers[i] - numbers[idx]) >= mid:
            count += 1
            idx = i
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(mid)

