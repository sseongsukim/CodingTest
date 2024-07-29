"""
점프와 순간이동
"""
def solution(N):
    answer = 1
    while N != 1:
        if N % 2 == 0:
            N /= 2
        else:
            answer += 1
            N -= 1
    return answer


print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5