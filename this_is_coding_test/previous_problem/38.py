"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""
N, M = map(int, input().split())
INF = int(1e9)
arr = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            arr[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

answer = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if arr[i][j] != INF or arr[j][i] != INF:
            count += 1

    if count == N:
        answer += 1

print(answer)