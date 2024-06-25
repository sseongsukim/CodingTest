"""
숫자 변환하기
List vs Set
"""
def solution(x, y, n):
    answer = 0
    possible_y = set()
    possible_y.add(x)
    while possible_y:
        if y in possible_y:
            return answer
        candidate = set()
        for py in possible_y:
            if py + n <= y:
                candidate.add(py + n)
            if py * 3 <= y:
                candidate.add(py * 3)
            if py * 2 <= y:
                candidate.add(py * 2)
        possible_y = candidate
        answer += 1
    return -1




print(solution(10, 40, 5)) # 2
print(solution(10, 40, 30)) # 1
print(solution(2, 5, 4)) # -1