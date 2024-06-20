"""
타겟 넘버
copy is much slower than just change the original list !
"""
from itertools import combinations


def solution(numbers, target):
    length = len(numbers)
    indices = [0] * length
    for i in range(length):
        indices[i] = i
    answer = 0
    for i in range(1, length):
        for case in list(combinations(indices, i)):
            for index in case:
                numbers[index] *= -1
            if sum(numbers) == target:
                answer += 1
            for index in case:
                numbers[index] *= -1
    return answer


print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4)) # 2