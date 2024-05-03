"""
10 -> 12
4 -> 4
"""
N = int(input())
next2, next3, next5 = 2, 3, 5
i2, i3, i5 = 1, 1, 1
dp = [0] * (N + 1)
dp[1] = 1

for n in range(2, N + 1):
    dp[n] = min(next2, next3, next5)
    if dp[n] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[n] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[n] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[N])