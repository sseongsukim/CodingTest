"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
"""
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0] * (N + 1)
max_value = 0
for n in range(N - 1, -1, -1):
    time = arr[n][0] + n
    if time <= N:
        dp[n] = max(arr[n][1] + dp[time], max_value)
        max_value = dp[n]
    else:
        dp[n] = max_value

print(max_value)