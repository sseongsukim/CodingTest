"""
리코쳇 로봇
"""
from collections import deque

def solution(board):
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                start_x, start_y = i, j
            elif board[i][j] == "G":
                goal_x, goal_y = i, j

    def after_move(x, y, d):
        if d == 0:
            while y < M:
                if board[x][y] == "D":
                    return x, y - 1
                y += 1
            y -= 1
        elif d == 1:
            while x >= 0:
                if board[x][y] == "D":
                    return x + 1, y
                x -= 1
            x += 1
        elif d == 2:
            while y >= 0:
                if board[x][y] == "D":
                    return x, y + 1
                y -= 1
            y += 1
        else:
            while x < N:
                if board[x][y] == "D":
                    return x - 1, y
                x += 1
            x -= 1

        return x, y

    q = deque()
    q.append((start_x, start_y))
    visited = [[-1] * M for _ in range(N)]
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = after_move(x, y, d)
            if visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited[goal_x][goal_y]

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])) # 7
print(solution([".D.R", "....", ".G..", "...D"])) # -1
