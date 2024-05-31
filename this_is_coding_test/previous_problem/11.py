"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
-> 9

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
-> 21
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
MAP = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x - 1][y - 1] = 1

T = int(input())
turns = {}
for _ in range(T):
    number, operator = input().split()
    turns[int(number)] = operator

# D => +1, L => -1
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

x, y = 0, 0
snake = [(x, y)]
MAP[x][y] = 2

time = 0
D = 0 # Right (0, 1)

while True:
    nx = x + direction[D % 4][0]
    ny = y + direction[D % 4][1]

    if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] != 2:
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = 2
            snake.append((nx, ny))
            px, py = snake.pop(0)
            MAP[px][py] = 0

        elif MAP[nx][ny] == 1:
            MAP[nx][ny] = 2
            snake.append((nx, ny))
    else:
        time += 1
        break

    x, y = nx, ny
    time += 1

    if time in turns.keys():
        if turns[time] == "L":
            D -= 1
        else:
            D += 1

print(time)







