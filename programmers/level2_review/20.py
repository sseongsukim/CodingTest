"""
n^2 배열 자르기
"""
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        index = (i // n, i % n)
        answer.append(max(index) + 1)
    return answer


print(solution(3, 2, 5)) # [3, 2, 2, 3]
print(solution(4, 7, 14)) # [4, 3, 3, 3, 4, 4, 4, 4]