"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
-> YES
"""
import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
MAP = []
teachers = []
students = []
blank = []
for x in range(N):
    MAP.append(list(input().split()))
    for y in range(N):
        if MAP[x][y] == "T":
            teachers.append((x, y))
        elif MAP[x][y] == "S":
            students.append((x, y))
        else:
            blank.append((x, y))

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def find_students(x, y, d):
    if d == 0:
        while y < N:
            if MAP[x][y] == "O":
                return False
            if MAP[x][y] == "S":
                return True
            y += 1
        return False
    elif d == 1:
        while x < N:
            if MAP[x][y] == "O":
                return False
            if MAP[x][y] == "S":
                return True
            x += 1
        return False
    elif d == 2:
        while y >= 0:
            if MAP[x][y] == "O":
                return False
            if MAP[x][y] == "S":
                return True
            y -= 1
        return False
    else:
        while x >= 0:
            if MAP[x][y] == "O":
                return False
            if MAP[x][y] == "S":
                return True
            x -= 1
        return False

for case in list(combinations(blank, 3)):
    for x, y in case:
        MAP[x][y] = "O"

    answer = False
    for tx, ty in teachers:
        for d in range(4):
            if find_students(tx, ty, d):
                answer = True
                break

    if not answer:
        break
    else:
        for x, y in case:
            MAP[x][y] = "X"

if not answer:
    print("YES")
else:
    print("NO")

print(MAP)