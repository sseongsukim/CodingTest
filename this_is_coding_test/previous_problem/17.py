"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
"""
from collections import deque
N, K = map(int, input().split())
arr = []
data = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] != 0:
            data.append((arr[i][j], 0, i, j))
S, X, Y = map(int, input().split())
data.sort(key= lambda x: x[0])
q = deque(data)
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while q:
    number, s, x, y = q.popleft()
    
    if s == S:
        break

    for d in range(4):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                arr[nx][ny] = number
                q.append((number, s + 1, nx, ny))

print(arr[X - 1][Y - 1])

