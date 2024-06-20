"""
게임 맵 최단거리

"""
from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    start_x, start_y = 0, 0
    visited[start_x][start_y] = True
    q = deque()
    q.append((start_x, start_y))
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maps[nx][ny] != 0:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    if visited[N - 1][M - 1]:
        return maps[N - 1][M - 1]
    else:
        return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1