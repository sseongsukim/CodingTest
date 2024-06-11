"""

"""

def solution(n):
    binary_scale_n = bin(n).split('b')[1]
    one_count = binary_scale_n.count("1")
    answer = n
    while True:
        answer += 1
        binary_scale_answer = bin(answer).split('b')[1]
        answer_one_count = binary_scale_answer.count("1")

        if answer_one_count == one_count:
            break
    return answer


print(solution(78)) # 83
print(solution(15)) # 23