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
import sys
from itertools import combinations
import copy
input = sys.stdin.readline
N = int(input())
arr = []
student = []
teacher = []
blank = []
for i in range(N):
    arr.append(list(input().split()))
    for j in range(N):
        if arr[i][j] == "S":
            student.append((i, j))
        elif arr[i][j] == "T":
            teacher.append((i, j))
        else:
            blank.append((i, j))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def find_student(arr, x, y, d):
    if d == 0:
        while y < N:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            y += 1
        return False
    elif d == 1:
        while x >= 0:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            x -= 1
        return False
    elif d == 2:
        while y >= 0:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            y -= 1
        return False
    else:
        while x < N:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            x += 1
        return False

def check(arr):
    for tx, ty in teacher:
        for d in range(4):
            if find_student(arr, tx, ty, d):
                return True
    return False


found = True
arr_copy = copy.deepcopy(arr)
for case in combinations(blank, 3):
    arr = copy.deepcopy(arr_copy)
    for new_wall in case:
        arr[new_wall[0]][new_wall[1]] = "O"

    if not check(arr):
        found = False
        break

if found:
    print("NO")
else:
    print("YES")

