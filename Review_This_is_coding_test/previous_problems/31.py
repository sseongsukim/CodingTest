"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    MAP = []
    for i in range(N):
        MAP.append(list(numbers[i * M: (i + 1) * M]))

    for j in range(1, M):
        for i in range(N):
            if i == 0:
                MAP[i][j] += max(MAP[i][j - 1], MAP[i + 1][j - 1])
            elif i == N - 1:
                MAP[i][j] += max(MAP[i][j - 1], MAP[i - 1][j - 1])
            else:
                MAP[i][j] += max(MAP[i][j - 1], MAP[i + 1][j - 1], MAP[i - 1][j - 1])

    max_value = -1e9
    for i in range(N):
        max_value = max(max_value, MAP[i][M - 1])
    print(max_value)