"""
7
15 11 4 8 5 2 4

6
50 20 30 10 20 10
"""
N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))