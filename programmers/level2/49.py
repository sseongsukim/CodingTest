"""
[1차] 프렌즈4블록

"""
import copy

def make_map(n, board):
    MAP = []
    for i in range(n):
        MAP.append(list(board[i]))
    return MAP

def find_indices(m, n, MAP):
    break_index = []
    for i in range(m):
        for j in range(n):
            if i + 1 < m and j + 1 < n:
                if MAP[i][j] == MAP[i + 1][j] == MAP[i][j + 1] == MAP[i + 1][j + 1] and MAP[i][j] != "X":
                    break_index.append((i, j))
                    break_index.append((i + 1, j))
                    break_index.append((i, j + 1))
                    break_index.append((i + 1, j + 1))
    return set(break_index)

def pull_down(m, n, MAP):
    while True:
        copy_map = copy.deepcopy(MAP)
        for i in range(1, m):
            for j in range(n):
                if MAP[i][j] == "X" and MAP[i - 1][j] != "X":
                    MAP[i][j] = MAP[i - 1][j]
                    MAP[i - 1][j] = "X"
        if copy_map == MAP:
            break
    return MAP

def solution(m, n, board):
    MAP = make_map(m, board)
    answer = 0
    while True:
        erase_indices = find_indices(m, n, MAP)
        if len(erase_indices) == 0:
            break
        else:
            answer += len(erase_indices)
        for indices in erase_indices:
            MAP[indices[0]][indices[1]] = "X"
        MAP = pull_down(m, n, MAP)
    return answer

print(solution(
    4, 5,
    ["CCBDE", "AAADE", "AAABF", "CCBBF"],
)) # 14
print(solution(
    6, 6,
    ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"],
)) # 15
