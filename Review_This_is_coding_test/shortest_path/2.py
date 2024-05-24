"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""
N, M = map(int, input().split())
INF = int(1e9)
arr = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            arr[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

X, K = map(int, input().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

answer = arr[1][K] + arr[K][X]
if answer >= INF:
    print(-1)
else:
    print(answer)