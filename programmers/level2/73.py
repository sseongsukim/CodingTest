"""
미로 탈출
Don't make visited
"""
from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])

    for i in range(N):
        for j in range(M):
            if maps[i][j] == "S":
                start_x, start_y = i, j
            elif maps[i][j] == "L":
                lever_x, lever_y = i, j
            elif maps[i][j] == "E":
                exit_x, exit_y = i, j

    direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    def get_distance(start_x, start_y, end_x, end_y):
        distance = [[0] * M for _ in range(N)]
        distance[start_x][start_y] = 0
        q = deque()
        q.append((start_x, start_y))
        past = False
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + direction[d][0]
                ny = y + direction[d][1]
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != "X" and not distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                    if nx == end_x and ny == end_y:
                        past = True
                        break

        if past:
            return distance[end_x][end_y]
        else:
            return -1

    start_to_lever = get_distance(start_x, start_y, lever_x, lever_y)
    lever_to_exit = get_distance(lever_x, lever_y, exit_x, exit_y)
    if -1 in [start_to_lever, lever_to_exit]:
        return -1
    else:
        return start_to_lever + lever_to_exit







print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1