"""
무인도 여행
"""
from collections import deque

def solution(maps):
    answer = []
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    N = len(maps)
    M = len(maps[0])
    MAP = []
    visited = [[False] * M for _ in range(N)]
    for n in range(N):
        MAP.append(list(maps[n]))

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        value = int(MAP[x][y])
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            for d in range(4):
                nx = x + direction[d][0]
                ny = y + direction[d][1]
                if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] != "X" and not visited[nx][ny]:
                    value += int(MAP[nx][ny])
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return value


    for x in range(N):
        for y in range(M):
            if MAP[x][y] != "X" and not visited[x][y]:
                answer.append(bfs(x, y))

    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)

print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1, 1, 27]
print(solution(["XXX","XXX","XXX"])) # [-1]