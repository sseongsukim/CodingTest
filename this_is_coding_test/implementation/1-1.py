"""
5
R R R U D D
"""
N = int(input())
x, y = 1, 1
moves = list(input().split())

for m in moves:
    if m == 'R':
        y += 1
        if y > N:
            y = N
    elif m == 'L':
        y -= 1
        if y < 1:
            y = 1
    elif m == 'U':
        x -= 1
        if x < 1:
            x = 1
    else:
        x += 1
        if x > N:
            x = N

print(x, y)