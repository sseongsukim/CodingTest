"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
-> 45
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
-> 55
"""
N = int(input())
Ts = []
Ps = []
for _ in range(N):
    t, p = map(int, input().split())
    Ts.append(t)
    Ps.append(p)

dp = [0] * N
max_value = 0
for i in range(N - 1, -1, -1):
    if i + Ts[i] > N:
        dp[i] = max_value
    else:
        max_value = max(max_value, dp[Ts[i] + i] + Ps[i])
        dp[i] = max_value

print(dp)