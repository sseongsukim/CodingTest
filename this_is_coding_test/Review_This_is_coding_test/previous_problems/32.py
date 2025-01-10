N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

for x in range(1, N):
    for y in range(x + 1):
        if y == 0:
            MAP[x][y] = MAP[x][y] + MAP[x - 1][y]
        elif y == x:
            MAP[x][y] = MAP[x][y] + MAP[x - 1][y - 1]
        else:
            MAP[x][y] = max(MAP[x][y] + MAP[x - 1][y - 1], MAP[x][y] + MAP[x - 1][y])

print(max(MAP[N - 1]))