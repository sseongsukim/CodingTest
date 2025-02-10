import sys
input = sys.stdin.readline

N = int(input())
MAP = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x][y] = 1

L = int(input())
commands = {}
for _ in range(L):
    time, command = input().split()
    commands[int(time)] = command

x, y = 0, 0
MAP[x][y] = 2
snake = [(x, y)]

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0

time = 0
while True:
    dx = x + direction[d % 4][0]
    dy = y + direction[d % 4][1]
    time += 1
    if 0 <= dx < N and 0 <= dy < N and MAP[dx][dy] != 2:
        if MAP[dx][dy] == 1:
            MAP[dx][dy] = 2
            snake.append((dx, dy))
            x, y = dx, dy
        else:
            MAP[dx][dy] = 2
            snake.append((dx, dy))
            px, py = snake.pop(0)
            MAP[px][py] = 0
            x, y = dx, dy
    else:
        break

    if time in commands.keys():
        if commands[time] == "L":
            d -= 1
        else:
            d += 1

print(time)