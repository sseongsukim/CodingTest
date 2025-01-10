"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""
N = int(input())
ts = []
ps = []
for i in range(N):
    t, p = map(int, input().split())
    ts.append(t)
    ps.append(p)

max_value = 0
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    time = ts[i] + i
    if time <= N:
        dp[i] = max(dp[time] + ps[i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max(dp))