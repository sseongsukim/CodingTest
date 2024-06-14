"""


"""
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n
        column = i % n
        number = max(row, column) + 1
        answer.append(number)
    return answer

print(solution(3, 2, 5)) # [3, 2, 2, 3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]