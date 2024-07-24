"""
다음 큰 숫쟈
"""
def solution(n):
    n_count = bin(n).split("b")[1].count("1")
    answer = n + 1
    while True:
        a_count = bin(answer).split("b")[1].count("1")
        if a_count == n_count:
            return answer
        else:
            answer += 1



print(solution(78)) # 83
print(solution(15)) # 23