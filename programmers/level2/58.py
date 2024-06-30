"""
삼각 달팽이

"""


def solution(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2, 3]

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + i

    max_value = dp[n]
    x, y = 0, 0
    direction = [[1, 0], [0, 1], [-1, -1]]
    d = 0
    MAP = [[0] * n for _ in range(n)]
    MAP[x][y] = 1
    value = 2
    while value != max_value + 1:
        nx = x + direction[d % 3][0]
        ny = y + direction[d % 3][1]
        if 0 <= nx < n and 0 <= ny < n and MAP[nx][ny] == 0:
            MAP[nx][ny] = value
            x, y = nx, ny
            value += 1
        else:
            d += 1
    answer = []
    for i in range(len(MAP)):
        for j in MAP[i]:
            if j != 0:
                answer.append(j)
    return answer

print(solution(4)) # [1,2,9,3,10,8,4,5,6,7]
print(solution(5)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]