"""
두 원 사이의 정수 쌍
"""
import math


def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        y_2 = math.floor(math.sqrt((r2 ** 2) - (x ** 2)))
        if x < r1:
            y_1 = math.ceil(math.sqrt((r1 ** 2) - (x ** 2)))
        else:
            y_1 = 0
        answer += (y_2 - y_1 + 1)
    return answer * 4

print(solution(2, 3))