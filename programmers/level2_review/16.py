"""
예상 대진표
"""
def solution(N, A, B):
    answer = 0
    while True:
        if A % 2 == 0:
            A /= 2
        else:
            A = (A + 1) / 2
        if B % 2 == 0:
            B /= 2
        else:
            B = (B + 1) / 2
        answer += 1
        if A == B:
            return answer


print(solution(8, 4, 7)) # 3