"""
N-Queen
"""
def dfs(queen, n, row):
    if n == row:
        return 1
    count = 0
    for col in range(n):
        queen[row] = col
        for x in range(row):
            if queen[x] == queen[row]:
                break
            if abs(queen[x] - queen[row]) == (row - x):
                break
        else:
            count += dfs(queen, n, row + 1)
    return count

def solution(n):
    queen = [0] * n
    return dfs(queen, n, 0)


print(solution(4))