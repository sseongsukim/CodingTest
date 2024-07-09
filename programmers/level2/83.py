"""
점 찍기

"""
def solution(k, d):
    answer = 0
    for y in range(0, d + 1, k):
        answer += ((d ** 2 - y ** 2) ** 0.5) // k + 1
    return int(answer)

print(solution(2, 4)) # 6
print(solution(1, 5)) # 26