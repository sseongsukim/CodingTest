"""
숫자 블록
"""
def get_divisor(num):
    if num == 1:
        return 0
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if num // i <= 10000000:
                return num // i
    if len(divisors) >= 1:
        return divisors[-1]
    return 1

def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(get_divisor(i))
    return answer

print(solution(1, 10)) # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]

