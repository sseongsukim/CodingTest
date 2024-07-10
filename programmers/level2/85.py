"""
과제 진행하기
"""
from collections import deque

def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = plans[i][1].split(":")
        start = int(h) * 60 + int(m)
        plans[i][1] = start
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])

    assign_q = deque()
    left_time = 0

    for i in range(len(plans)):
        name, start, playtime = plans[i]

        while assign_q:
            _name, _playtime = assign_q.pop()
            if left_time >= _playtime:
                left_time -= _playtime
                answer.append(_name)
            else:
                assign_q.append((_name, _playtime - left_time))
                break

        assign_q.append((name, playtime))

        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
            left_time = next_start - start

    while assign_q:
        _name, _ = assign_q.pop()
        answer.append(_name)

    return answer

print(solution(
    [
        ["korean", "11:40", "30"],
        ["english", "12:10", "20"],
        ["math", "12:30", "40"]
    ]
)) # ["korean", "english", "math"]

print(solution(
    [
        ["science", "12:40", "50"],
        ["music", "12:20", "40"],
        ["history", "14:00", "30"],
        ["computer", "12:30", "100"]
    ]
)) # ["science", "history", "computer", "music"]

print(solution([
    ["aaa", "12:00", "20"],
    ["bbb", "12:10", "30"],
    ["ccc", "12:40", "10"]
])) # ["bbb", "ccc", "aaa"]