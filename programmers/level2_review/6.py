"""
숫자의 표현
"""
def solution(n):
    answer = 0
    start = 1
    while start != n:
        value = 0
        for i in range(start, n + 1):
            value += i
            if value == n:
                answer += 1
            if value > n:
                break
        start += 1
    return answer + 1

print(solution(15)) # 4