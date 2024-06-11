"""
Note that
Conditioning in while loop is much faster than break using if function !
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
    answer += 1
    return answer


print(solution(15)) # 4
print(solution(14)) # 2