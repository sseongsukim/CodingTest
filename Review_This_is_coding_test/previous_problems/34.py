"""
7
15 11 4 8 5 2 4
"""
N = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()
dp = [1] * N

for i in range(N):
    for j in range(1, i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

