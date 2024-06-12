"""

"""
def solution(N):
    answer = 0
    while N > 1:
        if N % 2 == 0:
            N /= 2
        else:
            N -= 1
            answer += 1
    return answer + 1

print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5