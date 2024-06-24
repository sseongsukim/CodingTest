"""
방문 길이
가는길 오는길 확인!
"""
from collections import defaultdict

def solution(dirs):
    x, y = 0, 0
    answer = 0
    q = defaultdict(list)
    for d in dirs:
        key = (x, y)
        if d == "U":
            y += 1
            if y > 5:
                y = 5
        elif d == "D":
            y -= 1
            if y < -5:
                y = -5
        elif d == "R":
            x += 1
            if x > 5:
                x = 5
        elif d == "L":
            x -= 1
            if x < -5:
                x = -5
        value = (x, y)
        if key == value:
            continue
        if value not in q[key]:
            answer += 1
            q[key].append(value)
            q[value].append(key)

    return answer


print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7