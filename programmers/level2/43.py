"""
땅따먹기

"""
def solution(land):
    N = len(land)
    MAP = [[0] * 4 for _ in range(N)]
    MAP[0] = land[0]
    for i in range(1, N):
        for j in range(4):
            max_value = -1e9
            for k in range(4):
                if k == j:
                    continue
                max_value = max(max_value, MAP[i - 1][k])
            MAP[i][j] = max_value + land[i][j]

    return max(MAP[N - 1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) # 16