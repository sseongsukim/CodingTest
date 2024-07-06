"""
가장 큰 정사각형 찾기
"""

def solution(board):
    answer = board[0][0]

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 1 + min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])
                answer = max(answer, board[i][j])

    return answer ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9
print(solution([[0,0,1,1],[1,1,1,1]])) # 4