"""
4 6
19 15 10 17
"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

answer = 0
while start <= end:
    length = 0
    mid = (start + end) // 2
    for a in arr:
        if a > mid:
            length += (a - mid)

    if length > M:
        start = mid + 1
        answer = start
    else:
        end = mid - 1

print(answer)
