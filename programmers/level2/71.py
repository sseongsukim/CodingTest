"""
행렬 테두리 회전하기

"""
def solution(rows, columns, queries):
    answer = []
    MAP = [[0] * (columns + 1) for _ in range(rows + 1)]
    count = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            MAP[i][j] = count
            count += 1

    def change_map(MAP, start_x, start_y, end_x, end_y):
        new_map = [[0] * (columns + 1) for _ in range(rows + 1)]
        candidates = []
        for x in range(1, rows + 1):
            for y in range(1, columns + 1):
                if x == start_x and start_y < y <= end_y:
                    new_map[x][y] = MAP[x][y - 1]
                    candidates.append(MAP[x][y - 1])
                elif x == end_x and start_y <= y < end_y:
                    new_map[x][y] = MAP[x][y + 1]
                    candidates.append(MAP[x][y + 1])
                elif y == start_y and start_x <= x < end_x:
                    new_map[x][y] = MAP[x + 1][y]
                    candidates.append(MAP[x + 1][y])
                elif y == end_y and start_x < x <= end_x:
                    new_map[x][y] = MAP[x - 1][y]
                    candidates.append(MAP[x - 1][y])
                else:
                    new_map[x][y] = MAP[x][y]

        return new_map, candidates

    for start_x, start_y, end_x, end_y in queries:
        MAP, candidates = change_map(MAP, start_x, start_y, end_x, end_y)
        answer.append(min(candidates))
    return answer

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])) # [8, 10, 25]
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])) # [1, 1, 5, 3]
print(solution(100, 97, [[1, 1, 100, 97]])) # [1]