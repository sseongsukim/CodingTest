"""
10 -> 12
4 -> 4
"""
N = int(input())
next2, next3, next5 = 2, 3, 5
i2, i3, i5 = 1, 1, 1
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
        print(next2)
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp)
print(next2)
print(next3)
print(next5)


