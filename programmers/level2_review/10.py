"""
카펫
"""
def solution(brown, yellow):
    total = brown + yellow
    for x in range(2, total + 1):
        y = total / x
        if y % 1 == 0:
            if (x - 2) * (y - 2) == yellow:
                return [int(y), x]


print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]