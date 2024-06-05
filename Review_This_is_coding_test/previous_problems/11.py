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
N = int(input())
K = int(input())
apples = []
for _ in range(K):
    apples.append(list(map(int, input().split())))

L = int(input())
operators = {}
for _ in range(L):
    a, b = input().split()
    operators[int(a)] = b

MAP = [[0] * (N + 1) for _ in range(N + 1)]
for ax, ay in apples:
    MAP[ax][ay] = 1

D = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # Right, Down, Left, Up
x, y = 0, 0
snake = [(x, y)]
MAP[x][y] = 2
count = 0
while True:
    nx = direction[D % 4][0]
    ny = direction[D % 4][1]

    if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] != 2:
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = 2
            snake.append((nx, ny))
            px, py = snake.pop()
            MAP[px][py] = 0
        else:
            MAP[nx][ny] = 2
            snake.append((nx, ny))
    else:
        count += 1
        break

    if count in operators.keys():
        if operators[count] == "L":
            D -= 1
        else:
            D += 1

    count += 1
    x, y = nx, ny

print(count)
