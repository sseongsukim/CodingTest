"""
거리두기 확인하기

"""
from itertools import combinations

def check(p1, p2, walls):
    distance = get_distance(p1[0], p1[1], p2[0], p2[1])
    if distance <= 2:
        if p1[1] == p2[1]:
            if abs(p1[0] - p2[0]) == 1:
                return False
            if (min(p1[0], p2[0]) + 1, p1[1]) not in walls:
                return False
        elif p1[0] == p2[0]:
            if abs(p1[1] - p2[1]) == 1:
                return False
            if (p1[0], min(p1[1], p2[1]) + 1) not in walls:
                return False
        else:
            if (p2[1] - p1[1]) == (p2[0] - p1[0]):
                if (min(p1[0], p2[0]), max(p1[1], p2[1])) not in walls or (max(p1[0], p2[0]), min(p1[1], p2[1])) not in walls:
                    return False
            else:
                if (min(p1[0], p2[0]), min(p1[1], p2[1])) not in walls or (max(p1[0], p2[0]), max(p1[1], p2[1])) not in walls:
                    return False
    return True

def get_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def solution(places):
    N = 5
    TC = len(places)
    answer = []
    for t in range(TC):
        place = places[t]
        people = []
        walls = []
        for i in range(N):
            for j in range(N):
                if place[i][j] == "P":
                    people.append((i, j))
                elif place[i][j] == "X":
                    walls.append((i, j))

        following = 1
        for case in list(combinations(people, 2)):
            if following == 0:
                break
            p1, p2 = case
            if not check(p1, p2, walls):
                following = 0
                break

        answer.append(following)
    return answer




print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
])) # [1, 0, 1, 1, 1]