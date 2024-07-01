"""
124 나라의 숫자

"""
def solution(n):
    answer = ""
    cases = ['1', '2', '4']
    while n:
        n -= 1
        answer = cases[n % 3] + answer
        n //= 3
    return answer

print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
print(solution(4)) # 11
print(solution(10)) # 41