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
Ts = []
Ps = []
for _ in range(N):
    t, p = map(int, input().split())
    Ts.append(t)
    Ps.append(p)

max_value = 0
hours = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if i + Ts[i] > N:
        hours[i] = max_value
    else:
        hours[i] = max(Ps[i] + hours[Ts[i] + i], max_value)
        max_value = hours[i]

print(hours)
