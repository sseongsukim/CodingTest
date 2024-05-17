"""
4
1 3 1 5
"""
N = int(input())
arr = list(map(int, input().split()))
counts = [0] * (N + 1)

counts[1] = arr[0]
counts[2] = max(arr[0], arr[1])

for i in range(2, N + 1):
    counts[i] = max(counts[i - 1], counts[i - 2] + arr[i - 1])

print(counts[N])