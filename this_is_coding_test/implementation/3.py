"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
-> 3

3 3
1 1 0
1 1 1
1 0 0
1 1 0
-> 3
"""
N, M = map(int, input().split())
x, y, D = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
visited[x][y] = 1

# N, E, S, E (0, 1, 2, 3)
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
death = 0
count = 1
while True:
    nx = x + direction[D % 4][0]
    ny = y + direction[D % 4][1]
    if 0 <= nx < N and 0 <= ny < M:
        if visited[nx][ny] == 0 and arr[nx][ny] == 0:
            x, y = nx, ny
            count += 1
            death = 0
            visited[nx][ny] = 1
            continue
        else:
            death += 1

    D += 1

    if death == 4:
        nx = x - direction[D % 4][0]
        ny = y - direction[D % 4][1]
        if arr[nx][ny] == 0:
            x, y = nx, ny
            death = 0
        else:
            break

print(count)