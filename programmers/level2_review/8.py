"""
피보나치 수
"""
def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567
print(solution(3)) # 2
print(solution(5)) # 5