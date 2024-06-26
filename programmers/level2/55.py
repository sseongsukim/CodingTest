"""
소수 찾기

"""
from itertools import permutations

def check(x):
    x = int(x)
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    number_list = []
    for n in numbers:
        number_list.append(n)

    values = []
    for i in range(1, len(number_list) + 1):
        for case in list(permutations(number_list, i)):
            if case[0] == "0":
                continue
            value = "".join(case)
            if value not in values:
                values.append(value)
    answer = 0
    for value in values:
        if check(value):
            answer += 1
    return answer


print(solution("17")) # 3
print(solution("011")) # 2
