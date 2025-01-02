from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y, idx):
    total = MAP[x][y]
    count = 1
    candidates = [(x, y)]
    q = deque()
    q.append((x, y))
    union[x][y] = idx
    while q:
        x, y = q.popleft()
        for d in range(4):
            dx = x + direction[d][0]
            dy = y + direction[d][1]
            if 0 <= dx < N and 0 <= dy < N and L <= abs(MAP[dx][dy] - MAP[x][y]) <= R and union[dx][dy] == -1:
                q.append((dx, dy))
                union[dx][dy] = idx
                total += MAP[dx][dy]
                count += 1
                candidates.append((dx, dy))

    move_number = total // count
    for cx, cy in candidates:
        MAP[cx][cy] = move_number

answer = 0
while True:
    union = [[-1] * N for _ in range(N)]
    idx = 0
    for x in range(N):
        for y in range(N):
            if union[x][y] == -1:
                bfs(x, y, idx)
                idx += 1
    if idx == N * N:
        break
    answer += 1
print(answer)