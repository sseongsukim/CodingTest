"""
[3차] n진수 게임

"""
def radix_transformation(base: int, number: int) -> str:
    result = ""

    while number != 0:
        number, mod = divmod(number, base)

        if base > 10 and (10 <= mod <= 15):
            result += "ABCDEF"[mod % 10]
        else:
            result += str(mod)

    return result[::-1]

def solution(n, t, m, p):
    answer = ""
    answer_list = ["0"]

    total_step = t * m

    for i in range(1, total_step + 1):

        tr = radix_transformation(n, i)
        for t in range(len(tr)):
            answer_list.append(tr[t])
    answer_list = answer_list[:total_step]

    for i in range(len(answer_list)):
        if i % m + 1 == p:
            answer += answer_list[i]
    return answer


print(solution(2, 4, 2, 1)) # "0111"
print(solution(16, 16, 2, 1)) # "02468ACE11111111"
print(solution(16, 16, 2, 2)) # "13579BDF01234567"
print(solution(16, 16, 3, 2)) # "147ADA1316191111"