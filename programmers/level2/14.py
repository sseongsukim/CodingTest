"""


"""


def solution(n, a, b):
    answer = 1
    while n > 1:
        if a % 2 == 0:
            a /= 2
        else:
            a = (a + 1) / 2
        if b % 2 == 0:
            b /= 2
        else:
            b = (b + 1) / 2
        if a == b:
            break
        else:
            answer += 1
            n /= 2
    return answer

print(solution(8, 4, 7)) # 3