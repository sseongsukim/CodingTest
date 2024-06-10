
def solution(s):
    max_value = -1e9
    min_value = 1e9
    s = s.split(' ')
    for element in s:
        max_value = max(max_value, int(element))
        min_value = min(min_value, int(element))
    answer = f"{min_value} {max_value}"
    return answer

print(solution("1 2 3 4")) # "1 4"
print(solution("-1 -2 -3 -4")) # "-4 -1"
print(solution("-1 -1")) # "-1 -1"