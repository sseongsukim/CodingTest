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
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
MAP = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    MAP[x][y] = 1

L = int(input())
commands = {}
for _ in range(L):
    x, c = input().split()
    commands[int(x)] = c

x, y = 0, 0
snake = [(x, y)]
MAP[x][y] = 2

count = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0
while True:
    count += 1
    dx = x + direction[d % 4][0]
    dy = y + direction[d % 4][1]
    if 0 <= dx < N and 0 <= dy < N and MAP[dx][dy] != 2:
        if MAP[dx][dy] == 1:
            MAP[dx][dy] = 2
            snake.append((dx, dy))
        else:
            MAP[dx][dy] = 2
            snake.append((dx, dy))
            px, py = snake.pop(0)
            MAP[px][py] = 0
    else:
        break
    x, y = dx, dy
    if count in commands.keys():
        if commands[count] == "L":
            d -= 1
        else:
            d += 1
print(count)