"""
2 15
2
3

3 4
3
5
7
"""
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [10001] * (M + 1)
dp[0] = 0
for i in range(N):
    for j in range(arr[i], M + 1):
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

print(dp[M])