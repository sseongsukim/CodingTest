"""
최댓값과 최솟값
"""

def solution(s):
    s = s.split(" ")

    max_value = -1e9
    min_value = 1e9

    for num in s:
        if len(num) == 2:
            number = -1 * int(num[-1])
        else:
            number = int(num)
        min_value = min(number, min_value)
        max_value = max(number, max_value)
    answer = f"{min_value} {max_value}"
    return answer



print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))