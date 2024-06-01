"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X
"""
from itertools import combinations
import copy
import sys
input = sys.stdin.readline
N = int(input())
MAP = []
students = []
teachers = []
blanks = []
for i in range(N):
    MAP.append(list(input().split()))
    for j in range(N):
        if MAP[i][j] == "S":
            students.append((i, j))
        elif MAP[i][j] == "T":
            teachers.append((i, j))
        else:
            blanks.append((i, j))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def find_student(MAP, x, y, d):
    if d == 0:
        while y < N:
            if MAP[x][y] == "S":
                return True
            if MAP[x][y] == "O":
                return False
            y += 1

    elif d == 1:
        while x >= 0:
            if MAP[x][y] == "S":
                return True
            if MAP[x][y] == "O":
                return False
            x -= 1

    elif d == 2:
        while y >= 0:
            if MAP[x][y] == "S":
                return True
            if MAP[x][y] == "O":
                return False
            y -= 1

    else:
        while x < N:
            if MAP[x][y] == "S":
                return True
            if MAP[x][y] == "O":
                return False
            x += 1

    return False

def found(MAP):
    for tx, ty in teachers:
        for d in range(4):
            if find_student(MAP, tx, ty, d):
                return True
    return False

find = True
for case in list(combinations(blanks, 3)):
    NMAP = copy.deepcopy(MAP)
    for wx, wy in case:
        NMAP[wx][wy] = "O"

    if not found(NMAP):
        find = False
        break


if not find:
    print("YES")
else:
    print("NO")