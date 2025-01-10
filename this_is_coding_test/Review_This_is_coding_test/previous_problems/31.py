"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    MAP = []
    for i in range(1, N + 1):
        MAP.append(numbers[(i - 1) * M: i * M])

    for y in range(1, M):
        for x in range(N):
            if x == 0:
                MAP[x][y] = max(MAP[x][y] + MAP[x][y - 1], MAP[x][y] + MAP[x + 1][y - 1])
            elif x == N - 1:
                MAP[x][y] = max(MAP[x][y] + MAP[x][y - 1], MAP[x][y] + MAP[x - 1][y - 1])
            else:
                MAP[x][y] = max(MAP[x][y] + MAP[x][y - 1], MAP[x][y] + MAP[x - 1][y - 1], MAP[x][y] + MAP[x + 1][y - 1])

    answer = -1e9
    for x in range(N):
        answer = max(answer, MAP[x][M - 1])
    print(answer)