"""
26 -> 3

"""
N = int(input())
dp = [0] * (N + 1)
dp[1] = 0
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if dp[i] % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if dp[i] % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if dp[i] % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[N])