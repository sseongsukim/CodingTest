"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
arr = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            arr[i][j] = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    if cost < arr[a][b]:
        arr[a][b] = cost

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

print(arr)